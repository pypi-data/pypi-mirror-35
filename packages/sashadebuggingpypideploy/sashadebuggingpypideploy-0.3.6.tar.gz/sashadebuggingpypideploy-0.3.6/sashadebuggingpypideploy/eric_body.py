# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:23:52
# @Last Modified time: 2018-08-29 16:12:54
"""Check files for body.

Check, contains files of directory <body> or no.
"""
from erichek.eric_config import files_loop
from erichek.eric_config import pyfancy_critical
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_notice


def eric_body_function():
    """Check, contains body in a file, or no."""
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_pylint in files_loop():
        # Check if string in a file
        # https://stackoverflow.com/a/4944929/5951529
        # Encoding for Travis CI, see
        # https://stackoverflow.com/a/31492722/5951529
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354674238
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354681085
        if "<body>" in open(filename_pylint, encoding='utf-8').read():
            pyfancy_debug(filename_pylint + " contains <body>")

        else:
            pyfancy_critical("File " +
                             filename_pylint +
                             " not contain <body>. Please, add <body> in " +
                             filename_pylint +
                             ".")
            pyfancy_notice("If you see this message and, possibly, long output after them, "
                           "your file " + filename_pylint + " not contains <body>. "
                           "Please, add <body> to " + filename_pylint + " to correct place "
                           "and rerun erichek.")
            yield False


# def eric_body_summary():
#     """Report, contains <body> in all files or no."""
#     if False in [item for item in eric_body_function()]:
#         pyfancy_critical("Not all files contains <body>. Please, correct it.")
#         return False
#     pyfancy_notice("All files contains <body>")
#     return True
