# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-26 10:06:04
# @Last Modified time: 2018-08-24 08:16:06
"""Check files for correct head metadata.

Check, that files contains «Описание пакета:», «Процесс тренировки:» and so on.
"""
import os

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_error
from erichek.eric_config import pyfancy_notice

HEAD_DATA = True


def eric_head(head_metadata):
    """Check, that files contains metadata.

    Check for next metadata:

        + Описание пакета:
        + Процесс тренировки:
        + Примечания:
        + Пример вопроса 1:
        + Ответ к примеру вопроса 1:
        + Пример вопроса 2:
        + Ответ к примеру вопроса 2:
        + Источник(и):
        + Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):
        + Ссылка(и) на источник(и):
        + Постоянный адрес пакета:
    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:
        filename_without_path = os.path.basename(filename)

        # File content in folder
        each_file_in_folder = open(filename, encoding='utf-8').read()
        if head_metadata in each_file_in_folder:
            pyfancy_debug(
                '«' +
                head_metadata +
                '» contains in ' +
                filename_without_path)
        else:
            pyfancy_error(
                filename_without_path +
                ' not contains «' +
                head_metadata + '»')
            global HEAD_DATA
            HEAD_DATA = False


def eric_package_description():
    eric_head('Описание пакета:')


def eric_training_process():
    eric_head('Процесс тренировки:')


def eric_example_1():
    eric_head('Пример вопроса 1:')


def eric_example_1_answer():
    eric_head('Ответ к примеру вопроса 1:')


def eric_example_2():
    eric_head('Пример вопроса 2:')


def eric_example_2_answer():
    eric_head('Ответ к примеру вопроса 2:')


def eric_proof():
    eric_head('Источник(и):')


def eric_authors_and_editors():
    eric_head(
        'Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):')


def eric_prooflink():
    eric_head('Ссылка(и) на источник(и):')


def eric_package_link():
    eric_head('Постоянный адрес пакета:')


def eric_head_summary():
    """Report, contains head data in all files or no."""
    eric_package_description()
    eric_training_process()
    eric_example_1()
    eric_example_1_answer()
    eric_example_2()
    eric_example_2_answer()
    eric_proof()
    eric_authors_and_editors()
    eric_prooflink()
    eric_package_link()

    if HEAD_DATA:
        pyfancy_notice('All files contains correct head data')
    else:
        pyfancy_error(
            'One or more packages not contains one or more head data. Please, add correct head data to your package.')
