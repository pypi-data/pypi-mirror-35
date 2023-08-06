# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:23:52
# @Last Modified time: 2018-08-22 20:17:59
"""Check files for body.

Check, contains files of directory <body> or no.
"""
import erichek.eric_config
import os

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS
from erichek.eric_config import pyfancy_critical
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_notice

erichek.eric_config.LOG = os.path.splitext(os.path.basename(__file__))[0]

BODY_EXIST = True


def eric_body_function():
    """Check, contains body in a file, or no."""
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:

        filename_without_path = os.path.basename(filename)

        # Check if string in a file
        # https://stackoverflow.com/a/4944929/5951529
        # Encoding for Travis CI, see
        # https://stackoverflow.com/a/31492722/5951529
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354674238
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354681085
        if "<body>" in open(filename, encoding='utf-8').read():
            pyfancy_debug(filename_without_path + " contains <body>")

        else:
            pyfancy_critical("File " +
                             filename_without_path +
                             " not contain <body>. Please, add <body> in " +
                             filename_without_path +
                             ".")
            pyfancy_notice("If you see this message and, possibly, long output after them, "
                           "your file " + filename_without_path + " not contains <body>. "
                           "Please, add <body> to " + filename_without_path + " to correct place "
                           "and rerun erichek.")
            global BODY_EXIST
            BODY_EXIST = False


def eric_body_summary():
    """Report, contains <body> in all files or no.

    Use flags, see https://stackoverflow.com/a/48052480/5951529
    """
    eric_body_function()
    if BODY_EXIST:
        pyfancy_notice("All files contains <body>")

    if not BODY_EXIST:
        pyfancy_critical("Not all files contains <body>. Please, correct it.")
