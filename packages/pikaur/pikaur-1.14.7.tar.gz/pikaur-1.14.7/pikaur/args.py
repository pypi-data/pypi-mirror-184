"""Licensed under GPLv3, see https://www.gnu.org/licenses/"""

import sys
from argparse import Namespace
from pprint import pformat
from typing import Any, NoReturn

from .argparse import ArgumentParserWithUnknowns
from .config import PikaurConfig
from .i18n import translate, translate_many

ArgSchema = list[tuple[str | None, str, None | bool | str | int]]
PossibleArgValuesTypes = list[str] | str | bool | int | None


def debug(msg: str | None = None) -> None:
    sys.stderr.write(f'{msg or ""}\n')


def debug_format(msg: Any) -> None:
    debug(pformat(msg))


PACMAN_BOOL_OPTS: ArgSchema = [
    # sync options
    ("S", "sync", None),
    ("g", "groups", None),
    ("w", "downloadonly", None),
    ("q", "quiet", False),
    ("s", "search", None),
    ("d", "nodeps", None),
    # query options
    ("Q", "query", None),
    ("o", "owns", None),
    ("l", "list", None),  # @TODO
    (None, "upgrades", None),
    # operations
    ("D", "database", None),
    ("F", "files", None),
    ("R", "remove", None),
    ("T", "deptest", None),
    ("U", "upgrade", None),
    ("V", "version", None),
    ("h", "help", None),
    # universal options
    ("v", "verbose", None),
    (None, "debug", None),
    (None, "noconfirm", None),
    (None, "needed", False),
]


def get_pikaur_bool_opts() -> ArgSchema:
    return [
        (None, "noedit", PikaurConfig().review.NoEdit.get_bool()),
        (None, "edit", None),
        (None, "namesonly", False),
        (None, "repo", None),
        ("a", "aur", None),
        (None, "keepbuild", PikaurConfig().build.KeepBuildDir.get_bool()),
        (None, "keepbuilddeps", PikaurConfig().build.KeepBuildDeps.get_bool()),
        (None, "nodiff", PikaurConfig().review.NoDiff.get_bool()),
        (None, "rebuild", None),
        (None, "dynamic-users", PikaurConfig().build.AlwaysUseDynamicUsers.get_bool()),
        ("P", "pkgbuild", None),
        (None, "install", None),
        ("G", "getpkgbuild", None),
        (None, "deps", None),
        (None, "ignore-outofdate", PikaurConfig().sync.IgnoreOutofdateAURUpgrades.get_bool()),
        (None, "pikaur-debug", None),
        (None, "hide-build-log", None),
        (None, "print-commands", PikaurConfig().ui.PrintCommands.get_bool()),
        (None, "skip-failed-build", PikaurConfig().build.SkipFailedBuild.get_bool()),
        # undocumented options:
        (None, "print-args-and-exit", None),
    ]


PACMAN_STR_OPTS: ArgSchema = [
    (None, "color", None),
    ("b", "dbpath", None),  # @TODO: pyalpm?
    ("r", "root", None),
    (None, "arch", None),  # @TODO
    (None, "cachedir", None),  # @TODO
    (None, "config", None),
    (None, "gpgdir", None),
    (None, "hookdir", None),
    (None, "logfile", None),
    (None, "print-format", None),  # @TODO
]


def get_pikaur_str_opts() -> ArgSchema:
    return [
        (None, "build-gpgdir", PikaurConfig().build.GpgDir.get_str()),
        (None, "mflags", None),
        (None, "makepkg-config", None),
        (None, "makepkg-path", None),
        (None, "pikaur-config", None),
    ]


PACMAN_COUNT_OPTS: ArgSchema = [
    ("y", "refresh", 0),
    ("u", "sysupgrade", 0),
    ("c", "clean", 0),
    ("k", "check", 0),
    ("i", "info", 0),
]


def get_pikaur_count_opts() -> ArgSchema:
    return [
        (None, "devel", 0),
    ]


PACMAN_APPEND_OPTS: ArgSchema = [
    (None, "ignore", None),
    (None, "ignoregroup", None),  # @TODO
    (None, "overwrite", None),
    (None, "assume-installed", None),  # @TODO
]


def get_pikaur_long_opts() -> list[str]:
    return [
        long_opt.replace("-", "_")
        for _short_opt, long_opt, _default in (
            get_pikaur_bool_opts() + get_pikaur_str_opts() + get_pikaur_count_opts()
        )
    ]


def get_pacman_long_opts() -> list[str]:  # pragma: no cover
    return [
        long_opt.replace("-", "_")
        for _short_opt, long_opt, _default
        in PACMAN_BOOL_OPTS + PACMAN_STR_OPTS + PACMAN_COUNT_OPTS + PACMAN_APPEND_OPTS
    ]


class IncompatibleArgumentsError(Exception):
    pass


class MissingArgumentError(Exception):
    pass


class PikaurArgs(Namespace):
    unknown_args: list[str]
    raw: list[str]
    # typehints:
    info: bool | None
    nodeps: bool | None
    owns: bool | None
    check: bool | None
    ignore: list[str]
    makepkg_config: str | None
    mflags: str | None
    makepkg_path: str | None
    quiet: bool
    sysupgrade: int
    devel: int
    namesonly: bool
    build_gpgdir: str
    needed: bool
    config: str | None
    refresh: int
    clean: int
    # positional: List[str]
    # @TODO: pylint bug:
    positional: list[str] = []

    def __getattr__(self, name: str) -> PossibleArgValuesTypes:
        result: PossibleArgValuesTypes = getattr(
            super(),
            name,
            getattr(self, name.replace("-", "_"))
        )
        return result

    def handle_the_same_letter(self) -> None:
        # pylint: disable=attribute-defined-outside-init
        if self.pkgbuild and self.info:  # handle "-i"
            self.install = self.info
            self.info = False
        if (self.getpkgbuild or self.query) and self.nodeps:  # handle "-d"
            self.deps = self.nodeps
            self.nodeps = False
        if self.sync or self.pkgbuild:
            if self.owns:  # handle "-o"
                self.repo = self.owns
                self.owns = False
            if self.check:  # handle "-k"
                self.keepbuild = True
                self.check = None
        if self.sysupgrade:  # handle "-u"
            if self.query:
                self.sysupgrade = 0
                self.upgrades = True

    def post_process_args(self) -> None:
        # pylint: disable=attribute-defined-outside-init
        self.handle_the_same_letter()

        new_ignore: list[str] = []
        for ignored in self.ignore or []:
            new_ignore += ignored.split(",")
        self.ignore = new_ignore

        if self.debug:
            self.pikaur_debug = True

        if self.pikaur_debug or self.verbose:
            self.print_commands = True

    arg_depends = {
        "query": {
            "upgrades": ["aur", "repo", ],
        },
    }

    def validate(self) -> None:
        # pylint: disable=too-many-nested-blocks
        for operation, operation_depends in self.arg_depends.items():
            if getattr(self, operation):
                for arg_depend_on, dependant_args in operation_depends.items():
                    if not getattr(self, arg_depend_on):
                        for arg_name in dependant_args:
                            if getattr(self, arg_name):
                                raise MissingArgumentError(arg_depend_on, arg_name)

    @classmethod
    def from_namespace(
            cls,
            namespace: Namespace,
            unknown_args: list[str],
            raw_args: list[str]
    ) -> "PikaurArgs":
        result = cls()
        for key, value in namespace.__dict__.items():
            setattr(result, key, value)
        result.unknown_args = unknown_args
        result.raw = raw_args
        result.post_process_args()
        return result

    @property
    def raw_without_pikaur_specific(self) -> list[str]:
        result = self.raw[:]
        for arg in ("--pikaur-debug", ):
            if arg in result:
                result.remove(arg)
        return result


class PikaurArgumentParser(ArgumentParserWithUnknowns):

    def error(self, message: str) -> NoReturn:
        exc = sys.exc_info()[1]
        if exc:
            raise exc
        super().error(message)

    def parse_pikaur_args(self, raw_args: list[str]) -> PikaurArgs:
        parsed_args, unknown_args = self.parse_known_args(raw_args)
        for arg in unknown_args[:]:
            if arg.startswith("-"):
                continue
            unknown_args.remove(arg)
            parsed_args.positional.append(arg)
        return PikaurArgs.from_namespace(
            namespace=parsed_args,
            unknown_args=unknown_args,
            raw_args=raw_args
        )

    def add_letter_andor_opt(
            self,
            action: str | None = None,
            letter: str | None = None,
            opt: str | None = None,
            default: PossibleArgValuesTypes = None
    ) -> None:
        if action:
            if letter and opt:
                self.add_argument(
                    "-" + letter, "--" + opt, action=action, default=default
                )
            elif opt:
                self.add_argument(
                    "--" + opt, action=action, default=default
                )
            elif letter:
                self.add_argument(
                    "-" + letter, action=action, default=default
                )
        else:
            if letter and opt:
                self.add_argument(
                    "-" + letter, "--" + opt, default=default
                )
            elif opt:
                self.add_argument(
                    "--" + opt, default=default
                )
            elif letter:
                self.add_argument(
                    "-" + letter, default=default
                )


class CachedArgs():

    args: PikaurArgs | None = None


def debug_args(args: list[str], parsed_args: PikaurArgs) -> NoReturn:  # pragma: no cover
    debug("Input:")
    debug_format(args)
    debug()
    parsed_dict = vars(parsed_args)
    pikaur_long_opts = get_pikaur_long_opts()
    pacman_long_opts = get_pacman_long_opts()
    pikaur_dict = {}
    pacman_dict = {}
    misc_args = {}
    for arg, value in parsed_dict.items():
        if arg in pikaur_long_opts:
            pikaur_dict[arg] = value
        elif arg in pacman_long_opts:
            pacman_dict[arg] = value
        else:
            misc_args[arg] = value
    debug("PIKAUR parsed args:")
    debug_format(pikaur_dict)
    debug()
    debug("PACMAN parsed args:")
    debug_format(pacman_dict)
    debug()
    debug("MISC parsed args:")
    debug_format(misc_args)
    debug()
    debug("Reconstructed pacman args:")
    debug_format(reconstruct_args(parsed_args))
    debug()
    debug("Reconstructed pacman args without -S:")
    debug_format(reconstruct_args(parsed_args, ignore_args=["sync"]))
    sys.exit(0)


def parse_args(args: list[str] | None = None) -> PikaurArgs:
    if CachedArgs.args:
        return CachedArgs.args
    args = args or sys.argv[1:]
    parser = PikaurArgumentParser(prog=sys.argv[0], add_help=False)

    # add some of pacman options to argparser to have them registered by pikaur
    # (they will be bypassed to pacman with the rest unrecognized args anyway)

    for letter, opt, default in PACMAN_BOOL_OPTS + get_pikaur_bool_opts():
        parser.add_letter_andor_opt(
            action="store_true", letter=letter, opt=opt, default=default
        )

    for letter, opt, default in PACMAN_COUNT_OPTS + get_pikaur_count_opts():
        parser.add_letter_andor_opt(
            action="count", letter=letter, opt=opt, default=default
        )

    for letter, opt, default in PACMAN_APPEND_OPTS:
        parser.add_letter_andor_opt(
            action="append", letter=letter, opt=opt, default=default
        )

    for letter, opt, default in PACMAN_STR_OPTS + get_pikaur_str_opts():
        parser.add_letter_andor_opt(
            action=None, letter=letter, opt=opt, default=default
        )

    parser.add_argument("positional", nargs="*")

    parsed_args = parser.parse_pikaur_args(args)

    if parsed_args.positional and "-" in parsed_args.positional and not sys.stdin.isatty():
        parsed_args.positional.remove("-")
        parsed_args.positional += [
            word
            for line in sys.stdin.readlines()
            for word in line.split()
        ]

    if parsed_args.print_args_and_exit:  # pragma: no cover
        debug_args(args, parsed_args)

    try:
        parsed_args.validate()
    except IncompatibleArgumentsError as exc:
        debug(translate(":: error: options {} can't be used together.").format(
            ", ".join([f"'--{opt}'" for opt in exc.args])
        ))
        sys.exit(1)
    except MissingArgumentError as exc:
        debug(
            translate_many(
                ":: error: option {} can't be used without {}.",
                ":: error: options {} can't be used without {}.",
                len(exc.args[1:])
            ).format(
                ", ".join([f"'--{opt}'" for opt in exc.args[1:]]),
                f"'--{exc.args[0]}'"
            )
        )
        sys.exit(1)
    CachedArgs.args = parsed_args
    return parsed_args


def reconstruct_args(parsed_args: PikaurArgs, ignore_args: list[str] | None = None) -> list[str]:
    if not ignore_args:
        ignore_args = []
    for letter, opt, _default in (
            get_pikaur_bool_opts() + get_pikaur_str_opts() + get_pikaur_count_opts()
    ):
        if letter:
            ignore_args.append(letter)
        if opt:
            ignore_args.append(opt.replace("-", "_"))
    count_args = []
    for letter, opt, _default in PACMAN_COUNT_OPTS:
        if letter:
            count_args.append(letter)
        if opt:
            count_args.append(opt.replace("-", "_"))
    reconstructed_args = {
        f"--{key}" if len(key) > 1 else f"-{key}": value
        for key, value in vars(parsed_args).items()
        if value
        if key not in ignore_args + count_args + [
            "raw", "unknown_args", "positional",  # computed members
        ] + [
            long_arg
            for _short_arg, long_arg, default in PACMAN_STR_OPTS + PACMAN_APPEND_OPTS
        ]
    }
    result = list(set(
        list(reconstructed_args.keys()) + parsed_args.unknown_args
    ))
    for args_key, value in vars(parsed_args).items():
        for letter, _opt, _default in PACMAN_COUNT_OPTS:
            opt = _opt.replace("-", "_")
            if value and opt == args_key and opt not in ignore_args and letter not in ignore_args:
                result += ["--" + opt] * value
    return result
