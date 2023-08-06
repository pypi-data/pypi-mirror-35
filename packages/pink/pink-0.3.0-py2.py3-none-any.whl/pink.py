#!/usr/bin/env python
# coding=utf-8

import os
import sys

import glob2
import black

PEP8_MAXLINE = 79


def command_line_runner():
    """
    主函数
    """
    python = sys.executable
    black_exec = black.__file__.rstrip("cdo")

    path = sys.argv[1:]
    for p in path:
        for file in glob2.glob(p):
            print(file)
            os.popen(
                f"{python} {black_exec} {file} --line-length {PEP8_MAXLINE}"
            ).read()
            print()
    sys.exit()


if __name__ == "__main__":
    command_line_runner()
