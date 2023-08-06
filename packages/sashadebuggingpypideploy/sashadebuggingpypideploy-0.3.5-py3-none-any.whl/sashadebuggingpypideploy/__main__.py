# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:32:05
# @Last Modified time: 2018-08-26 08:28:27
"""Run tests.

Main file for running Erichek tests.
"""
import erichek.eric_body as eric_body
import erichek.eric_encoding as eric_encoding
import erichek.eric_eyo as eric_eyo
import erichek.eric_head as eric_head
import erichek.eric_regex as eric_regex

from clize import run
from erichek.eric_config import clize_log_level
from erichek.eric_config import pyfancy_error
from erichek.eric_config import pyfancy_notice
from erichek.eric_config import v
from erichek.eric_config import version

# ASCII-art printing
# [BUG] ASCII-ART output, when --help or --version
# https://github.com/epsy/clize/issues/38#issue-290426111
# https://stackoverflow.com/a/9638532/5951529
# import sys
# from colorama import init
# from pyfiglet import figlet_format
# from termcolor import cprint

# strip colors if stdout is redirected
# init(strip=not sys.stdout.isatty())


def main():
    """Run Erichek.

    Run all modules of Erichek.
    If no errors — validation success,
    Else — exit(1).

    [NOTE] Do not use “exit=False” or “exit=True” in “run” function!
    https://github.com/epsy/clize/issues/33#issuecomment-354849918
    If “exit=True”, “erichek” will not work;
    else “exit=False”, all erichek modules will run, if “erichek --version” will run.
    """
    run(clize_log_level, alt=[version, v], exit=False)
    eric_encoding.eric_encoding_summary()
    eric_body.eric_body_summary()
    eric_eyo.eric_eyo_summary()
    eric_regex.eric_regex_summary()
    eric_head.eric_head_summary()

    # If all instead of multiple if and:
    # https://stackoverflow.com/a/9504681/5951529
    if all([eric_body.BODY_EXIST, eric_encoding.ENCODING_UTF_8, eric_regex.REGEX_DATA,
            eric_eyo.EYO_YO, eric_head.HEAD_DATA]):
        pyfancy_notice(
            "Congratulations! You haven't errors in your packages!")
        # cprint(figlet_format('\nSuccess', font='starwars'),
        # 'white', 'on_green', attrs=['bold'])
    else:
        pyfancy_error(
            "You have errors in your packages. Please, fix them.")
        # cprint(figlet_format('\nFailure', font='starwars'),
        # 'yellow', 'on_red', attrs=['bold'])
        exit(1)


if __name__ == '__main__':
    main()
