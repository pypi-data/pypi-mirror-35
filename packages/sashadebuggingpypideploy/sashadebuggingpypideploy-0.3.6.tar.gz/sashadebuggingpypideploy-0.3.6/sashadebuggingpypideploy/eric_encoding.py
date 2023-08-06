# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 18:30:38
# @Last Modified time: 2018-08-30 15:53:37
"""Encoding checker.

Check, that files in Windows-1251 encoding.

Bugs:
    1. if no Cyrillic symbols in a file, chardet detect file encoding as ASCII;
    2. chardet can detect Windows-1251 as MacCyrillic.
"""
import codecs

import chardet

from erichek.eric_config import files_loop
from erichek.eric_config import pyfancy_critical
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_notice

# [DEPRECATED] Use yield and return for variables passing.
# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
# ENCODING_UTF_8 = True


def eric_encoding_function():
    """Check encoding of the file.

    chardet check, that each file in Windows-1251.
    MacCyrillic — also true.
    In local testing UTF-8 convert to Cyrillic-1251.
    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_pylint in files_loop():

        # Not 100%, see https://stackoverflow.com/a/436299/5951529
        # Can doesn't work for Latin packages
        # Check decoding — http://bit.ly/2C3xSUD
        # https://stackoverflow.com/a/37531241/5951529
        rawdata = open(filename_pylint, "rb").read()
        chardet_data = chardet.detect(rawdata)
        # Python dictionary
        fileencoding = (chardet_data['encoding'])

        # [DEPRECATED] Migrating from Cyrillic 1251 to UTF-8
        # chardet_confidence = (chardet_data['confidence'])
        # # Needs MacCyrillic, because chardet can check Windows-1251
        # # as MacCyrillic
        # if fileencoding == 'windows-1251':
        #     LOG.debug(filename_without_path + " in windows-1251 encoding")
        # # Integer to string:
        # # https://stackoverflow.com/a/961638/5951529
        # elif fileencoding == 'MacCyrillic':
        #     LOG.info(pyfancy().green("Encoding of file " + filename_without_path +
        #                              " chardet detect as MacCyrillic with confidence " +
        #                              str(chardet_confidence)))
        # else:
        #     # Convert file from UTF-8 to Cyrillic 1251
        #     # https://stackoverflow.com/q/19932116/5951529
        #     with codecs.open(filename, "r", "utf-8") as file_for_conversion:
        #         read_file_for_conversion = file_for_conversion.read()
        #     with codecs.open(filename, "w", "windows-1251") as file_for_conversion:
        #         if read_file_for_conversion:
        #             file_for_conversion.write(read_file_for_conversion)
        #     red_background(filename_without_path +
        #                    " in " +
        #                    fileencoding +
        #                    ", not in Windows-1251 encoding! Please, save " +
        #                    filename_without_path + " in Windows-1251 encoding.")
        #     green_foreground("If encoding of file " + filename_without_path +
        #                      " is UTF-8 and you see message above in local wwtd testing, " +
        #                      filename_without_path +
        #                      " automatically will converted from UTF-8 to Windows-1251.")
        #     Use flags:
        #     https://stackoverflow.com/a/48052480/5951529
        #     global ENCODING_WINDOWS_1251
        #     ENCODING_WINDOWS_1251 = False
        if fileencoding == 'utf-8':
            pyfancy_debug(filename_pylint + " in UTF-8 encoding")
        else:
            # Convert file from Cyrillic 1251 to UTF-8
            # https://stackoverflow.com/q/19932116/5951529
            with codecs.open(filename_pylint, "r", "windows-1251") as file_for_conversion:
                read_file_for_conversion = file_for_conversion.read()
            with codecs.open(filename_pylint, "w", "utf-8") as file_for_conversion:
                if read_file_for_conversion:
                    file_for_conversion.write(read_file_for_conversion)
            pyfancy_critical(filename_pylint +
                             " in " +
                             fileencoding +
                             ", not in UTF-8 encoding! Please, save " +
                             filename_pylint + " in UTF-8 encoding.")
            pyfancy_notice("If encoding of file " + filename_pylint +
                           " is Windows-1251 and you see message above in local wwtd testing, " +
                           filename_pylint +
                           " automatically will converted from Windows-1251 to UTF-8.")
            yield False


# def eric_encoding_summary():
#     """Report, all files in UTF-8 or no."""
#     if False in [item for item in eric_encoding_function()]:
#         pyfancy_critical(
#             "One or more your files not in UTF-8 encoding. Please, convert it (them) to UTF-8.")
#         return False
#     pyfancy_notice("All files in UTF-8 encoding")
#     return True
