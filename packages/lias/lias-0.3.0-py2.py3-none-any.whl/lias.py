# encoding=utf8

import argparse
import os
import subprocess
import sys

import glob2

VERSION = "0.3.0"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description="Format imports via command line with `isort`"
    )
    parser.add_argument(
        "paths",
        metavar="PATHS",
        type=str,
        nargs="*",
        help="Files and directories that should be executed format command.",
    )
    parser.add_argument(
        "-sp",
        "--settings_path",
        type=str,
        default="",
        help="Explicitly set the settings path instead of auto "
             "determining based on file location",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Displays the current version of lias",
    )
    return parser


def command_line_runner():
    """
    主函数
    """
    python = sys.executable

    parser = get_parser()
    args = vars(parser.parse_args())
    if args["version"]:
        print(VERSION)
        return

    paths = args["paths"]
    if not paths:
        parser.print_help()
        return

    settings = args["settings_path"]
    if settings:
        settings = os.path.abspath(settings)

    cnt = 0
    print("Sorting imports...")
    for path in paths:
        for file in glob2.glob(path):
            cnt += 1
            subprocess.Popen(
                f"isort {file} -sp {settings}",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
    print("All {} files done! ✨✨".format(cnt))
    sys.exit()


if __name__ == "__main__":
    command_line_runner()
