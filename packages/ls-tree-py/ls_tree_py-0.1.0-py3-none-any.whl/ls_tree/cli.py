import os
import re
import sys
from itertools import islice
from pathlib import Path

# alias t="venv/bin/poetry run ls-tree | less -R"

space = "    "
line = "│   "
tee = "├─ "
knee = "└─ "

IGNORE_RE = re.compile(r"^(\.(git|idea|venv|tox)|venv|__pycache__)$")


class Colors:
    blue_back = "\033[0;44m"
    bold = "\033[1m"
    bright_black = "\033[0;90m"
    bright_blue = "\033[0;94m"
    bright_purple = "\033[0;35m"
    bright_red = "\033[0;91m"
    bright_white = "\033[0;97m"
    cyan_back = "\033[0;46m"
    dark_blue = "\033[0;34m"
    dark_cyan = "\033[0;36m"
    dark_green = "\033[0;32m"
    darken = "\033[2m"
    dull_white = "\033[0;37m"
    green_back = "\033[0;42m"
    grey = "\x1b[90m"
    gray = "\033[38;4;236m"
    grey_back = "\033[0;40m"
    invisible = "\033[08m"
    italic = "\033[3m"
    light_cyan = "\033[0;96m"
    light_green = "\033[0;92m"
    magenta = "\033[0;95m"
    orange = "\033[0;33m"
    orange_back = "\033[0;43m"
    pink_back = "\033[0;41m"
    pure_black = "\033[0;30m"
    pure_red = "\033[0;31m"
    purple_back = "\033[0;45m"
    reset = "\033[0m"
    reverse = "\033[07m"
    underline = "\033[4m"
    white_back = "\033[0;47m"
    yellow = "\033[0;93m"


def render_item(path: Path) -> str:
    if path.is_symlink():
        d = "/" if path.is_dir() else ""
        return Colors.bright_purple + path.name + Colors.reset + "@" + " -> " + str(path.readlink()) + d
    elif path.is_dir():
        return "".join(
            [
                Colors.bright_blue,
                path.name,
                Colors.reset,
                "/",
                "..." if IGNORE_RE.match(path.name) else "",
            ]
        )
    elif os.access(path.absolute(), os.X_OK):
        return Colors.pure_red + path.name + Colors.reset + "*"
    elif path.name.endswith(".py"):
        return Colors.dark_green + Colors.darken + path.name + Colors.reset
    else:
        return path.name


# https://stackoverflow.com/a/59109706/179581
def tree(
    dir_path: Path, level: int = -1, limit_to_directories: bool = False, length_limit: int = 1000
):
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path)  # accept string coerceable to Path
    files = 0
    directories = 0

    def inner(dir_path: Path, prefix: str = "", level: int = -1):
        nonlocal files, directories
        if not level:
            return  # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else:
            contents = sorted(list(dir_path.iterdir()))
        pointers = [tee] * (len(contents) - 1) + [knee]
        for pointer, path in zip(pointers, contents):
            pp = Colors.darken + prefix + pointer + Colors.reset
            if path.is_dir() and not path.is_symlink():
                yield pp + render_item(path)
                directories += 1
                extension = line if pointer == tee else space

                if not IGNORE_RE.match(path.name):
                    yield from inner(path, prefix=prefix + extension, level=level - 1)
            elif not limit_to_directories:
                yield pp + render_item(path)
                files += 1

    print(Colors.bright_white + Colors.bold + str(dir_path.absolute()) + Colors.reset)
    iterator = inner(dir_path, level=level)
    for ln in islice(iterator, length_limit):
        print(ln)
    if next(iterator, None):
        print(f"... length_limit, {length_limit}, reached, counted:")
    print(f"\n{directories} directories" + (f", {files} files" if files else ""))


def run(*args):
    path = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    # import glob
    # r = glob.glob(path)
    # print(sys.argv)
    # print(r)

    # for line in tree(Path(path)):
    #     print(line)

    tree(Path(path), level=4)


if __name__ == "__main__":
    pass
