"""Licensed under GPLv3, see https://www.gnu.org/licenses/"""

import os
import shutil
from glob import glob
from multiprocessing.pool import ThreadPool
from typing import TYPE_CHECKING

from .args import PikaurArgs, parse_args
from .aur import find_aur_packages, get_repo_url
from .config import (
    AUR_REPOS_CACHE_PATH,
    BUILD_CACHE_PATH,
    BUILD_DEPS_LOCK,
    PACKAGE_CACHE_PATH,
    PikaurConfig,
)
from .core import (
    PIPE,
    DataType,
    InteractiveSpawn,
    dirname,
    interactive_spawn,
    isolate_root_cmd,
    joined_spawn,
    open_file,
    remove_dir,
    replace_file,
    running_as_root,
    spawn,
    sudo,
)
from .exceptions import BuildError, CloneError, DependencyError, DependencyNotBuiltYetError, SysExit
from .filelock import FileLock
from .i18n import translate, translate_many
from .makepkg_config import MakePkgCommand, MakepkgConfig, get_pkgdest
from .pacman import PackageDB, ProvidedDependency, get_pacman_command, install_built_deps
from .pprint import (
    ColorsHighlight,
    bold_line,
    color_enabled,
    color_line,
    create_debug_logger,
    print_error,
    print_stderr,
    print_stdout,
)
from .prompt import (
    ask_to_continue,
    get_editor_or_exit,
    get_input,
    retry_interactive_command_or_exit,
)
from .srcinfo import SrcInfo
from .updates import is_devel_pkg
from .urllib import wrap_proxy_env
from .version import VersionMatcher, compare_versions

if TYPE_CHECKING:
    from .core import SpawnArgs


_debug = create_debug_logger("build")


class PkgbuildChanged(Exception):  # noqa: N818
    pass


def _shell(cmds: list[str]) -> InteractiveSpawn:
    return interactive_spawn(isolate_root_cmd(wrap_proxy_env(cmds)))


def _mkdir(to_path: str) -> None:
    mkdir_result = spawn(isolate_root_cmd(["mkdir", "-p", to_path]))
    if mkdir_result.returncode != 0:
        print_stdout(mkdir_result.stdout_text)
        print_stderr(mkdir_result.stderr_text)
        raise Exception(translate(f"Can't create destination directory '{to_path}'."))


def copy_aur_repo(from_path: str, to_path: str) -> None:
    from_path = os.path.realpath(from_path)
    to_path = os.path.realpath(to_path)
    if not os.path.exists(to_path):
        _mkdir(to_path)

    from_paths = []
    for src_path in glob(f"{from_path}/*") + glob(f"{from_path}/.*"):
        if os.path.basename(src_path) != ".git":
            from_paths.append(src_path)
    to_path = f"{to_path}/"

    cmd_args = isolate_root_cmd(["cp", "-r"] + from_paths + [to_path])

    result = spawn(cmd_args)
    if result.returncode != 0:
        if os.path.exists(to_path):
            remove_dir(to_path)
            _mkdir(to_path)
        result = interactive_spawn(cmd_args)
        if result.returncode != 0:
            raise Exception(translate(f"Can't copy '{from_path}' to '{to_path}'."))


class PackageBuild(DataType):  # pylint: disable=too-many-public-methods
    # pylint: disable=too-many-instance-attributes
    clone = False
    pull = False

    package_base: str
    package_names: list[str]

    repo_path: str
    pkgbuild_path: str
    build_dir: str
    build_gpgdir: str
    built_packages_paths: dict[str, str]

    reviewed = False
    keep_build_dir = False
    skip_carch_check = False
    _source_repo_updated = False
    _build_files_copied = False

    failed: bool | None = None

    new_deps_to_install: list[str]
    new_make_deps_to_install: list[str]
    built_deps_to_install: dict[str, str]

    args: PikaurArgs
    resolved_conflicts: list[list[str]] | None = None

    _local_pkgs_wo_build_deps: set[str]
    _local_pkgs_with_build_deps: set[str]
    _local_provided_pkgs_with_build_deps: dict[str, list[ProvidedDependency]]

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} "{self.package_base}" '
            f"{self.package_names}>"
        )

    def __init__(  # pylint: disable=super-init-not-called
            self,
            package_names: list[str] | None = None,
            pkgbuild_path: str | None = None
    ) -> None:
        self.args = parse_args()

        if pkgbuild_path:
            self.repo_path = dirname(pkgbuild_path)
            self.pkgbuild_path = pkgbuild_path
            srcinfo = SrcInfo(pkgbuild_path=pkgbuild_path)
            srcinfo.regenerate()  # @TODO: this is a workaround for building
            # multiple PKGBUILDs from the same directory, find some better way.
            pkgbase = srcinfo.get_value("pkgbase")
            if pkgbase and srcinfo.pkgnames:
                self.package_names = package_names or srcinfo.pkgnames
                self.package_base = pkgbase
            else:
                no_pkgname_error = translate("Can't get package name from PKGBUILD")
                raise BuildError(no_pkgname_error)
        elif package_names:
            self.package_names = package_names
            self.package_base = find_aur_packages([package_names[0]])[0][0].packagebase
            self.repo_path = os.path.join(AUR_REPOS_CACHE_PATH, self.package_base)
            self.pkgbuild_path = os.path.join(self.repo_path, "PKGBUILD")
        else:
            missing_property_error = translate(
                "Either `{prop1}` or `{prop2}` should be set"
            ).format(
                prop1="package_names",
                prop2="pkgbuild_path",
            )
            raise NotImplementedError(missing_property_error)

        self.build_dir = os.path.join(BUILD_CACHE_PATH, self.package_base)
        self.build_gpgdir = self.args.build_gpgdir
        self.built_packages_paths = {}
        self.keep_build_dir = self.args.keepbuild or (
            is_devel_pkg(self.package_base) and PikaurConfig().build.KeepDevBuildDir.get_bool()
        )
        self.skip_carch_check = PikaurConfig().build.IgnoreArch.get_bool()

        if os.path.exists(self.repo_path):
            if os.path.exists(os.path.join(self.repo_path, ".git")):
                self.pull = True
            else:
                self.clone = True
        else:
            os.makedirs(self.repo_path)
            self.clone = True

        self.reviewed = self.current_hash == self.last_installed_hash

        self._local_pkgs_wo_build_deps = set()
        self._local_pkgs_with_build_deps = set()
        self._local_provided_pkgs_with_build_deps = {}

    def git_reset_changed(self) -> InteractiveSpawn:
        return _shell([
            "git",
            "-C", self.repo_path,
            "checkout",
            "--",
            "*"
        ])

    def git_stash(self) -> InteractiveSpawn:
        return _shell([
            "git",
            "-C", self.repo_path,
            "stash",
        ])

    def git_stash_pop(self) -> InteractiveSpawn:
        return _shell([
            "git",
            "-C", self.repo_path,
            "stash",
            "pop",
        ])

    def update_aur_repo(self) -> InteractiveSpawn:
        cmd_args: list[str]
        if self.pull:
            cmd_args = [
                "git",
                "-C", self.repo_path,
                "pull",
                "origin",
                "master"
            ]
        if self.clone:
            cmd_args = [
                "git",
                "clone",
                get_repo_url(self.package_base),
                self.repo_path,
            ]
        if not cmd_args:
            return NotImplemented
        result = spawn(isolate_root_cmd(wrap_proxy_env(cmd_args)))
        self.reviewed = self.current_hash == self.last_installed_hash
        return result  # noqa: RET504

    @property
    def last_installed_file_path(self) -> str:
        return os.path.join(
            self.repo_path,
            "last_installed.txt"
        )

    @property
    def last_installed_hash(self) -> str | None:
        """Commit hash of AUR repo of last version of the pkg installed by Pikaur."""
        if os.path.exists(self.last_installed_file_path):
            with open_file(self.last_installed_file_path) as last_installed_file:
                lines = last_installed_file.readlines()
                if lines:
                    return lines[0].strip()
        return None

    def update_last_installed_file(self) -> None:
        git_hash_path = os.path.join(
            self.repo_path,
            ".git/refs/heads/master"
        )
        if os.path.exists(git_hash_path):
            shutil.copy2(
                git_hash_path,
                self.last_installed_file_path
            )

    @property
    def current_hash(self) -> str | None:
        """Commit hash of AUR repo of the pkg."""
        git_hash_path = os.path.join(
            self.repo_path,
            ".git/refs/heads/master"
        )
        if not os.path.exists(git_hash_path):
            return None
        with open_file(git_hash_path) as current_hash_file:
            return current_hash_file.readlines()[0].strip()

    def get_latest_dev_sources(self, *, check_dev_pkgs: bool = True) -> None:
        if not self.reviewed:
            return
        self.prepare_build_destination()
        if (
                self._source_repo_updated
        ) or (
            not (is_devel_pkg(self.package_base) and check_dev_pkgs)
        ):
            return
        print_stdout("{} {}...".format(  # pylint: disable=consider-using-f-string
            color_line("::", ColorsHighlight.white),
            translate_many(
                "Downloading the latest sources for a devel package {}",
                "Downloading the latest sources for devel packages {}",
                len(self.package_names)
            ).format(
                bold_line(", ".join(self.package_names))
            )
        ))
        pkgver_result = joined_spawn(
            isolate_root_cmd(
                MakePkgCommand.get() + [
                    "--nobuild", "--nocheck", "--nodeps"
                ],
                cwd=self.build_dir
            ),
            cwd=self.build_dir,
        )
        if pkgver_result.returncode != 0:
            error_text = translate("failed to retrieve latest dev sources:")
            print_error(error_text)
            print_stderr(pkgver_result.stdout_text)
            if (
                    not self.args.skip_failed_build
            ) and (
                not ask_to_continue(default_yes=False)
            ):
                raise BuildError(error_text)
        SrcInfo(self.build_dir).regenerate()
        self._source_repo_updated = True

    def get_version(self, package_name: str) -> str:
        return SrcInfo(self.build_dir, package_name).get_version()

    def _compare_versions(self, compare_to: int) -> bool:
        local_db = PackageDB.get_local_dict()
        self.get_latest_dev_sources(check_dev_pkgs=self.args.needed)
        return min(
            compare_versions(
                local_db[pkg_name].version,
                self.get_version(pkg_name)
            ) == compare_to
            if pkg_name in local_db else False
            for pkg_name in self.package_names
        )

    @property
    def version_already_installed(self) -> bool:
        return self._compare_versions(0)

    @property
    def version_is_upgradeable(self) -> bool:
        return self._compare_versions(-1)

    @property
    def all_deps_to_install(self) -> list[str]:
        return self.new_make_deps_to_install + self.new_deps_to_install

    def _filter_built_deps(
            self,
            all_package_builds: dict[str, "PackageBuild"]
    ) -> None:

        def _mark_dep_resolved(dep: str) -> None:
            if dep in self.new_make_deps_to_install:
                self.new_make_deps_to_install.remove(dep)
            if dep in self.new_deps_to_install:
                self.new_deps_to_install.remove(dep)

        all_provided_pkgnames: dict[str, str] = {}
        for pkg_build in all_package_builds.values():
            for pkg_name in pkg_build.package_names:
                srcinfo = SrcInfo(
                    pkgbuild_path=pkg_build.pkgbuild_path, package_name=pkg_name
                )
                all_provided_pkgnames.update({
                    provided_name: pkg_name
                    for provided_name in
                    [pkg_name] + srcinfo.get_values("provides")
                })

        self.built_deps_to_install = {}

        for dep in self.all_deps_to_install:
            dep_name = VersionMatcher(dep).pkg_name
            if dep_name not in all_provided_pkgnames:
                continue
            package_build = all_package_builds[all_provided_pkgnames[dep_name]]
            if package_build == self:
                _mark_dep_resolved(dep)
                continue
            for pkg_name in package_build.package_names:
                if package_build.failed:
                    self.failed = True
                    raise DependencyError()
                if not package_build.built_packages_paths.get(pkg_name):
                    raise DependencyNotBuiltYetError()
                self.built_deps_to_install[pkg_name] = \
                    package_build.built_packages_paths[pkg_name]
                _mark_dep_resolved(dep)

    def _get_pacman_command(self, ignore_args: list[str] | None = None) -> list[str]:
        return get_pacman_command(ignore_args=ignore_args) + (
            ["--noconfirm"] if self.args.noconfirm else []
        )

    def install_built_deps(
            self,
            all_package_builds: dict[str, "PackageBuild"]
    ) -> None:

        self.get_deps(all_package_builds)
        if not self.built_deps_to_install:
            return

        print_stderr("{} {}:".format(  # pylint: disable=consider-using-f-string
            color_line("::", ColorsHighlight.purple),
            translate("Installing already built dependencies for {}").format(
                bold_line(", ".join(self.package_names)))
        ))

        try:
            update_self_deps = False
            for pkg_name, pkg_build in all_package_builds.items():
                if pkg_name in self.built_deps_to_install:
                    pkg_build.install_built_deps(all_package_builds)
                    update_self_deps = True
            if update_self_deps:
                self.get_deps(all_package_builds)
            install_built_deps(
                deps_names_and_paths=self.built_deps_to_install,
                resolved_conflicts=self.resolved_conflicts
            )
        except DependencyError as dep_exc:
            self.failed = True
            raise dep_exc from None
        finally:
            PackageDB.discard_local_cache()

    def _set_built_package_path(self) -> None:
        pkg_paths_spawn = spawn(
            isolate_root_cmd(MakePkgCommand.get() + ["--packagelist"],
                             cwd=self.build_dir),
            cwd=self.build_dir
        )
        if pkg_paths_spawn.returncode != 0:
            return
        if not pkg_paths_spawn.stdout_text:
            return
        pkg_paths = pkg_paths_spawn.stdout_text.splitlines()
        if not pkg_paths:
            return
        pkg_dest = get_pkgdest()
        pkg_paths.sort(key=len)
        for pkg_name in self.package_names:
            pkg_path = pkg_paths[0]
            if len(pkg_paths) > 1:
                arch = MakepkgConfig.get("CARCH")
                for each_path in pkg_paths:
                    each_filename = os.path.basename(each_path)
                    if pkg_name in each_filename and (
                            (f"-{arch}." in each_filename) or ("-any." in each_filename)
                    ):
                        pkg_path = each_filename
                        break
            pkg_filename = os.path.basename(pkg_path)
            if pkg_path == pkg_filename:
                pkg_path = os.path.join(pkg_dest or self.build_dir, pkg_path)
            if not pkg_dest or MakePkgCommand.pkgdest_skipped:
                new_package_path = os.path.join(pkg_dest or PACKAGE_CACHE_PATH, pkg_filename)
                pkg_sig_path = pkg_path + ".sig"
                new_package_sig_path = new_package_path + ".sig"
                if not os.path.exists(PACKAGE_CACHE_PATH):
                    os.makedirs(PACKAGE_CACHE_PATH)
                replace_file(pkg_path, new_package_path)
                replace_file(pkg_sig_path, new_package_sig_path)
                pkg_path = new_package_path
            if pkg_path and os.path.exists(pkg_path):
                self.built_packages_paths[pkg_name] = pkg_path

    def check_if_already_built(self) -> bool:
        self.get_latest_dev_sources()
        self._set_built_package_path()
        if (
                not self.args.rebuild and
                len(self.built_packages_paths) == len(self.package_names)
        ):
            print_stderr("{} {}\n".format(  # pylint: disable=consider-using-f-string
                color_line("::", ColorsHighlight.green),
                translate_many(
                    "Package {pkg} is already built. Pass '--rebuild' flag to force the build.",
                    "Packages {pkg} are already built. Pass '--rebuild' flag to force the build.",
                    len(self.package_names)
                ).format(
                    pkg=bold_line(", ".join(self.package_names))
                )
            ))
            return True
        return False

    def prepare_build_destination(self, *, flush: bool = False) -> None:
        if flush:
            remove_dir(self.build_dir)
            self._build_files_copied = False
        if self._build_files_copied:
            return
        if os.path.exists(self.build_dir) and not self.keep_build_dir:
            remove_dir(self.build_dir)
        copy_aur_repo(self.repo_path, self.build_dir)

        pkgbuild_name = os.path.basename(self.pkgbuild_path)
        if pkgbuild_name != "PKGBUILD":
            default_pkgbuild_path = os.path.join(self.build_dir, "PKGBUILD")
            custom_pkgbuild_path = os.path.join(self.build_dir, pkgbuild_name)
            if os.path.exists(default_pkgbuild_path):
                os.unlink(default_pkgbuild_path)
            os.renames(custom_pkgbuild_path, default_pkgbuild_path)
        self._build_files_copied = True

    def get_deps(
            self,
            all_package_builds: dict[str, "PackageBuild"],
            *,
            filter_built: bool = True,
            exclude_pkg_names: list[str] | None = None,
    ) -> None:
        exclude_pkg_names = exclude_pkg_names or []
        self.new_deps_to_install = []
        new_make_deps_to_install: list[str] = []
        new_check_deps_to_install: list[str] = []
        for package_name in self.package_names:
            if package_name in exclude_pkg_names:
                continue
            src_info = SrcInfo(pkgbuild_path=self.pkgbuild_path, package_name=package_name)
            for new_deps_version_matchers, deps_destination in (
                    (
                        src_info.get_build_depends(), self.new_deps_to_install
                    ), (
                        src_info.get_build_makedepends(), new_make_deps_to_install,
                    ), (
                        src_info.get_build_checkdepends(), new_check_deps_to_install,
                    ),
            ):
                # find deps satisfied explicitly:
                new_deps_to_install = [
                    dep_line
                    for dep_lines in [
                        new_deps_version_matchers[dep_name].line.split(",")
                        for dep_name in PackageDB.get_not_found_local_packages([
                            vm.line for vm in new_deps_version_matchers.values()
                        ])
                    ]
                    for dep_line in dep_lines
                ]
                deps_destination += new_deps_to_install
        self.new_make_deps_to_install = list(set(
            new_make_deps_to_install + new_check_deps_to_install
        ))
        if filter_built:
            self._filter_built_deps(all_package_builds)

    def _install_repo_deps(self) -> None:
        if not self.all_deps_to_install:
            return

        print_stderr("{} {}:".format(  # pylint: disable=consider-using-f-string
            color_line("::", ColorsHighlight.purple),
            translate("Installing repository dependencies for {}").format(
                bold_line(", ".join(self.package_names)))
        ))

        retry_interactive_command_or_exit(
            sudo(
                self._get_pacman_command() + [
                    "--sync",
                    "--asdeps",
                ] + self.all_deps_to_install
            ),
            pikspect=True,
            conflicts=self.resolved_conflicts,
        )
        PackageDB.discard_local_cache()
        self._local_pkgs_with_build_deps = set(PackageDB.get_local_dict().keys())
        self._local_provided_pkgs_with_build_deps = PackageDB.get_local_provided_dict()

    def install_all_deps(self, all_package_builds: dict[str, "PackageBuild"]) -> None:
        with FileLock(BUILD_DEPS_LOCK):
            self.get_deps(all_package_builds)
            if self.all_deps_to_install or self.built_deps_to_install:
                PackageDB.discard_local_cache()
                self._local_pkgs_wo_build_deps = set(PackageDB.get_local_dict().keys())
            self.install_built_deps(all_package_builds)
            self._install_repo_deps()

    def _remove_installed_deps(self) -> None:
        if not self._local_pkgs_wo_build_deps:
            return

        _debug("Gonna compute diff of installed pkgs")
        deps_packages_installed = self._local_pkgs_with_build_deps.difference(
            self._local_pkgs_wo_build_deps
        )
        deps_packages_removed = self._local_pkgs_wo_build_deps.difference(
            self._local_pkgs_with_build_deps
        )
        _debug(f"{deps_packages_installed=}")
        _debug(f"{deps_packages_removed=}")
        if not deps_packages_installed:
            return

        # check if there is diff incosistency because of the package replacement:
        if deps_packages_removed:
            for removed_pkg_name in list(deps_packages_removed):
                for installed_pkg_name in list(deps_packages_installed):
                    if (
                            removed_pkg_name in self._local_provided_pkgs_with_build_deps
                    ) and (
                        installed_pkg_name
                        in [
                            dep.name for dep
                            in self._local_provided_pkgs_with_build_deps[removed_pkg_name]
                        ]
                    ):
                        deps_packages_installed.remove(installed_pkg_name)
                        deps_packages_removed.remove(removed_pkg_name)
                        continue

        if deps_packages_removed:
            error_text = translate(
                "Failed to remove installed dependencies, packages inconsistency: {}"
            ).format(
                bold_line(", ".join(deps_packages_removed))
            )
            print_error(error_text)
            if not ask_to_continue():
                raise DependencyError(error_text)
        if not deps_packages_installed or self.args.keepbuilddeps:
            return

        print_stderr("{} {}:".format(  # pylint: disable=consider-using-f-string
            color_line("::", ColorsHighlight.purple),
            translate("Removing already installed dependencies for {}").format(
                bold_line(", ".join(self.package_names)))
        ))
        retry_interactive_command_or_exit(
            sudo(
                # pacman --remove flag conflicts with some --sync options:
                self._get_pacman_command(ignore_args=[
                    "overwrite",
                ]) + [
                    "--remove",
                ] + list(deps_packages_installed)
            ),
            pikspect=True,
        )
        PackageDB.discard_local_cache()

    def check_pkg_arch(self) -> None:
        if self.skip_carch_check:
            return

        src_info = SrcInfo(pkgbuild_path=self.pkgbuild_path)
        arch = MakepkgConfig.get("CARCH")
        supported_archs = src_info.get_values("arch")
        if supported_archs and (
                "any" not in supported_archs
        ) and (
            arch not in supported_archs
        ):
            error_text = translate(
                (
                    "{name} can't be built on the current arch ({arch}). "
                    "Supported: {suparch}"
                )
            ).format(
                name=bold_line(", ".join(self.package_names)),
                arch=arch,
                suparch=", ".join(supported_archs)
            )
            print_error(error_text)
            if (
                    not self.args.skip_failed_build
            ) and (
                not ask_to_continue(default_yes=False)
            ):
                raise BuildError(error_text)
            self.skip_carch_check = True

    def build_with_makepkg(self) -> bool:  # pylint: disable=too-many-branches,too-many-statements
        makepkg_args = []
        if not self.args.needed:
            makepkg_args.append("--force")
        if not color_enabled():
            makepkg_args.append("--nocolor")

        print_stderr("\n{} {}:".format(  # pylint: disable=consider-using-f-string
            color_line("::", ColorsHighlight.purple),
            translate("Starting the build")
        ))
        build_succeeded = False
        skip_pgp_check = False
        skip_file_checksums = False
        skip_check = False
        no_prepare = False
        while True:
            cmd_args = MakePkgCommand.get() + makepkg_args
            if skip_pgp_check:
                cmd_args += ["--skippgpcheck"]
            if skip_file_checksums:
                cmd_args += ["--skipchecksums"]
            if self.skip_carch_check:
                cmd_args += ["--ignorearch"]
            if skip_check:
                cmd_args += ["--nocheck"]
            if no_prepare:
                cmd_args += ["--noprepare"]

            env = {}
            if self.build_gpgdir != "":
                env["GNUPGHOME"] = self.build_gpgdir

            cmd_args = isolate_root_cmd(cmd_args, cwd=self.build_dir, env=env)
            spawn_kwargs: "SpawnArgs" = {
                "cwd": self.build_dir,
                "env": {**os.environ, **env},
            }
            if self.args.hide_build_log:
                spawn_kwargs.update({
                    "stdout": PIPE,
                    "stderr": PIPE
                })

            result = interactive_spawn(
                cmd_args,
                **spawn_kwargs
            )
            print_stdout()
            build_succeeded = result.returncode == 0
            if build_succeeded:
                break

            print_stderr(
                color_line(
                    translate("Command '{}' failed to execute.").format(
                        " ".join(cmd_args)
                    ),
                    ColorsHighlight.red
                )
            )
            if self.args.skip_failed_build:
                answer = translate("s")
            elif self.args.noconfirm:
                answer = translate("a")
            else:  # pragma: no cover
                prompt = "{} {}\n{}\n> ".format(
                    color_line("::", ColorsHighlight.yellow),
                    translate("Try recovering?"),
                    "\n".join((
                        translate("[R] retry build"),
                        translate("[p] PGP check skip"),
                        translate("[c] checksums skip"),
                        translate("[f] skip 'check()' function of PKGBUILD"),
                        translate("[n] skip 'prepare()' function of PKGBUILD"),
                        translate("[i] ignore architecture"),
                        translate("[d] delete build dir and try again"),
                        translate("[e] edit PKGBUILD"),
                        "-" * 24,
                        translate("[s] skip building this package"),
                        translate("[a] abort building all the packages"),
                    ))
                )
                answer = get_input(
                    prompt,
                    translate("r").upper() +
                    translate("p") +
                    translate("c") +
                    translate("f") +
                    translate("n") +
                    translate("i") +
                    translate("d") +
                    translate("e") +
                    translate("s") +
                    translate("a")
                )

            answer = answer.lower()[0]
            if answer == translate("r"):  # pragma: no cover
                continue
            if answer == translate("p"):  # pragma: no cover
                skip_pgp_check = True
                continue
            if answer == translate("c"):  # pragma: no cover
                skip_file_checksums = True
                continue
            if answer == translate("f"):  # pragma: no cover
                skip_check = True
                continue
            if answer == translate("n"):  # pragma: no cover
                no_prepare = True
                continue
            if answer == translate("i"):  # pragma: no cover
                self.skip_carch_check = True
                continue
            if answer == translate("d"):  # pragma: no cover
                self.prepare_build_destination(flush=True)
                continue
            if answer == translate("e"):  # pragma: no cover
                editor_cmd = get_editor_or_exit()
                if editor_cmd:
                    interactive_spawn(
                        editor_cmd + [self.pkgbuild_path]
                    )
                    interactive_spawn(isolate_root_cmd([
                        "cp",
                        self.pkgbuild_path,
                        os.path.join(self.build_dir, "PKGBUILD")
                    ]))
                    raise PkgbuildChanged()
                continue
            if answer == translate("a"):
                raise SysExit(125)
            # "s"kip
            break

        return build_succeeded

    def build(
            self,
            all_package_builds: dict[str, "PackageBuild"],
            resolved_conflicts: list[list[str]]
    ) -> None:
        self.resolved_conflicts = resolved_conflicts

        self.prepare_build_destination()

        self.install_all_deps(all_package_builds)
        try:
            if self.check_if_already_built():
                build_succeeded = True
            else:
                build_succeeded = self.build_with_makepkg()
        finally:
            self._remove_installed_deps()

        if not build_succeeded:
            self.failed = True
            raise BuildError()
        self._set_built_package_path()


def clone_aur_repos(package_names: list[str]) -> dict[str, PackageBuild]:
    aur_pkgs, _ = find_aur_packages(package_names)
    packages_bases: dict[str, list[str]] = {}
    for aur_pkg in aur_pkgs:
        packages_bases.setdefault(aur_pkg.packagebase, []).append(aur_pkg.name)
    package_builds_by_base = {
        pkgbase: PackageBuild(pkg_names)
        for pkgbase, pkg_names in packages_bases.items()
    }
    package_builds_by_name = {
        pkg_name: package_builds_by_base[pkgbase]
        for pkgbase, pkg_names in packages_bases.items()
        for pkg_name in pkg_names
    }
    pool_size: int | None = None
    if running_as_root():
        pool_size = 1
    with ThreadPool(processes=pool_size) as pool:
        requests = {
            key: pool.apply_async(repo_status.update_aur_repo, ())
            for key, repo_status in package_builds_by_base.items()
        }
        pool.close()
        pool.join()
        for package_base, request in requests.items():
            result = request.get()
            if result.returncode > 0:
                raise CloneError(
                    build=package_builds_by_base[package_base],
                    result=result
                )
    return package_builds_by_name
