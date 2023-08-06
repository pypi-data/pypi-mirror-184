"""
Command-line script to show information about available tasks
"""

import sys
import argparse

from typing import List, TextIO


from .. import VERSION
from ..api import PiiFinder
from ..api.file import add_taskfile
from ..helper.taskdict import language_list, country_list
from ..helper.plugins import list_plugins


def print_tasks(proc: PiiFinder, out: TextIO):
    print(f". Installed tasks [language={proc.lang}]", file=out)
    for (pii, country), tasklist in proc.task_info().items():
        print(f"\n {pii.name}  [country={country}]   ", file=out)
        for name, doc in tasklist:
            print(f"     {name}: {doc}", file=out)


def print_plugins(lang: str, out: TextIO):
    print(f". Installed plugins [language={lang}]", file=out)
    for plugin in list_plugins(lang):
        print(f"\n {plugin['name']}  {plugin['version']}   ", file=out)
        desc = plugin.get('description')
        if desc:
            print("  ", desc)

def process(
    lang: str,
    country: List[str] = None,
    tasks: List[str] = None,
    all_tasks: bool = False,
    taskfile: List[str] = None,
    debug: bool = False,
    **kwargs,
):
    """
    Process the request: show task info
    """
    # Create the object
    proc = PiiFinder(lang, country, tasks, all_tasks=all_tasks, debug=debug)
    if taskfile:
        add_taskfile(taskfile, proc)
    if kwargs.get('list_plugins'):
        print_plugins(proc, sys.stdout)

    # Show tasks
    print_tasks(proc, sys.stdout)


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"Show information about available PII tasks (version {VERSION})"
    )

    opt_com1 = argparse.ArgumentParser(add_help=False)
    c1 = opt_com1.add_argument_group('Selction options')
    c1.add_argument("--lang", help="language", required=True)
    c1.add_argument("--country", nargs="+",
                    help="countries to use (use 'all' for all countries defined for the language)")

    opt_com2 = argparse.ArgumentParser(add_help=False)
    c2 = opt_com2.add_argument_group("Other")
    c2.add_argument("--debug", action="store_true", help="debug mode")
    c2.add_argument('--verbose', '-v', type=int, default=3,
                    help='verbose level (0-5). Default: %(default)d')
    c2.add_argument('--reraise', action='store_true',
                    help='re-raise exceptions on errors')


    subp = parser.add_subparsers(help='command', dest='cmd')

    s0 = subp.add_parser('list-languages', parents=[c2],
                         help="List all defined languages")

    s1 = subp.add_parser("list-plugins", parents=[c1, c2],
                         help="List all installed piim plugins")

    s2 = subp.add_parser("list-tasks", parents=[c1, c2])
    g2 = s2.add_argument_group("Task specification")
    g21 = g2.add_mutually_exclusive_group(required=True)
    g21.add_argument(
        "--tasks", metavar="TASK_NAME", nargs="+", help="pii tasks to include"
    )
    g21.add_argument(
        "--all-tasks", action="store_true", help="add all pii tasks available"
    )
    g2.add_argument(
        "--taskfile", nargs="+", help="add all pii tasks defined in a JSON file"
    )

    parsed = parser.parse_args(args)
    return parsed


def main(args: List[str] = None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    if args.cmd == "list-plugins":
        print_plugins(args.lang, sys.stdout)
    elif args.cmd == "list-languages":
        for lang in language_list():
            print(f"  {lang}:", " ".join(country_list(lang)))
    else:
        args = vars(args)
        process(args.pop("lang"), **args)


if __name__ == "__main__":
    main()
