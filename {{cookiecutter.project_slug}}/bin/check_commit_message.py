#!/usr/bin/env python
import argparse
import atexit
from pathlib import Path

PREFIXES = {
    "docs": "docs or typos",
    "tests": "testing",
    "core": "project core",
    "command-line": "command line, __main__",
    "scripts": "internal scripts",
    "misc": "other",
    "release": "releases",
}


def check():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path, help="commit file")
    args = parser.parse_args()

    print(args.file)
    with open(args.file) as file:
        commit = file.read().strip().split("\n")[0]

    if commit.startswith("Merge"):
        exit(0)
    prefix, _, message = commit.rpartition(":")
    if not prefix:
        print("No prefix specified!")
        exit(1)
    if not message:
        print("Empty commit messages are not allowed!")
        exit(1)
    if prefix not in PREFIXES.keys():
        print("Unknown prefix!")
        exit(1)


if __name__ == "__main__":
    try:
        check()
    except SystemExit as e:
        if e.code != 0:
            print(
                "Please read docs/contributing.md for more details about commit style."
            )
        raise
