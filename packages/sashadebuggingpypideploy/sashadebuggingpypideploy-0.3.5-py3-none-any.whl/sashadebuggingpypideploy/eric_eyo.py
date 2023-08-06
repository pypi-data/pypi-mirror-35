# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-08-12 07:52:00
# @Last Modified time: 2018-08-22 20:23:06
import _locale
import delegator
import erichek.eric_config
import os
import sys

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_error
from erichek.eric_config import pyfancy_notice

erichek.eric_config.LOG = os.path.splitext(os.path.basename(__file__))[0]

# Set Windows locale to UTF-8:
# https://stackoverflow.com/a/34345136/5951529
# https://github.com/kennethreitz/delegator.py/blob/7420834967ead70bf65bc1270c88f7a3a352df2b/delegator.py#L78-L88
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

EYO_YO = True


def eric_eyo():
    """Check files, that «ё» contains

    Check files, use «eyo» checker:
    https://www.npmjs.com/package/eyo
    """
    for filename in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:
        filename_without_path = os.path.basename(filename)
        eyo_command = delegator.run(
            'eyo --lint --only-safe ' + filename_without_path)
        if eyo_command.return_code == 22:
            pyfancy_error("«ё» replacing needs in " + filename_without_path)
            # Different commands for Windows and *NIX:
            # https://www.quora.com/Can-I-run-my-Python-program-in-both-Linux-and-Windows
            # eyo not support in-place replacing:
            # https://github.com/hcodes/eyo/issues/15
            # No built-in cross-platforms tools for file moving.
            if sys.platform == 'Windows':
                delegator.run(
                    'eyo ' +
                    filename_without_path +
                    ' > temp && move temp ' +
                    filename_without_path)
            else:
                delegator.run(
                    'eyo ' +
                    filename_without_path +
                    ' > temp && mv temp ' +
                    filename_without_path)
            global EYO_YO
            EYO_YO = False
        else:
            pyfancy_debug("eyo did not find any gross errors related to «ё» in the file " +
                          filename_without_path)


def eric_eyo_summary():
    eric_eyo()
    if EYO_YO:
        pyfancy_notice("All files contains «ё»")
    else:
        pyfancy_error("One or more your files doesn't contain «ё». Please, make your changes locally.")
