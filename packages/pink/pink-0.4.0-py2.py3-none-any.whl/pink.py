#!/usr/bin/env python
# coding=utf-8

import os
import sys
import argparse

import glob2
import black

PEP8_MAXLINE = 79
VERSION = "0.4.0"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description="Format code via command line with `black`"
    )
    parser.add_argument(
        "paths",
        metavar="PATHS",
        type=str,
        nargs="*",
        help="Files and directories that should be executed format command.",
    )
    parser.add_argument(
        "-l",
        "--line",
        type=int,
        default=PEP8_MAXLINE,
        help="How many character per line to allow.[default: 79]",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Displays the current version of pink",
    )
    return parser


def command_line_runner():
    """
    主函数
    """
    python = sys.executable
    black_exec = black.__file__.rstrip("cdo")

    parser = get_parser()
    args = vars(parser.parse_args())
    if args["version"]:
        print(VERSION)
        return

    paths = args["paths"]
    maxline = args["line"]
    if not paths:
        parser.print_help()
        return
    for path in paths:
        for file in glob2.glob(path):
            print(file)
            os.popen(
                f"{python} {black_exec} {file} --line-length {maxline}"
            ).read()
            print()
    sys.exit()


if __name__ == "__main__":
    command_line_runner()
