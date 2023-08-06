# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-26 10:06:04
# @Last Modified time: 2018-08-30 16:23:12
"""Check files for correct head metadata.

Check, that files contains «Описание пакета:», «Процесс тренировки:» and so on.
"""
from erichek.eric_config import files_loop
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_error


def eric_head(head_metadata):
    """Check, that files contains metadata.

    Wrapper, contains certain metadata in files or no.
    Lists and generators differences:
    https://www.severcart.org/blog/all/understanding_yield_in_Python/

    Arguments:
        head_metadata {str} -- metadata of Erichek rooms string

    Yields:
        bool -- return False, if any error in any file

    """
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename_pylint in files_loop():
        if head_metadata in open(filename_pylint, encoding='utf-8').read():
            pyfancy_debug(
                '«' +
                head_metadata +
                '» contains in ' +
                filename_pylint)
        else:
            pyfancy_error(
                filename_pylint +
                ' not contains «' +
                head_metadata + '»')
            yield False


def eric_package_link():
    """Check «Постоянный адрес пакета:».

    Python >= 3.3, PEP 380: yield from is equivalent:
    for item in iterable:
        yield item
    https://pythonworld.ru/novosti-mira-python/chto-novogo-v-python-33.html

    yield always return generator:
    https://stackoverflow.com/a/25313357/5951529
    """
    yield from eric_head('Постоянный адрес пакета:')


def eric_package_description():
    """Check «Описание пакета:»."""
    yield from eric_head('Описание пакета:')


def eric_training_process():
    """Check «Процесс тренировки:»."""
    yield from eric_head('Процесс тренировки:')


def eric_example_1():
    """Check «Пример вопроса 1:»."""
    yield from eric_head('Пример вопроса 1:')


def eric_example_1_answer():
    """Check «Ответ к примеру вопроса 1:»."""
    yield from eric_head('Ответ к примеру вопроса 1:')


def eric_example_2():
    """Check «Пример вопроса 2:»."""
    yield from eric_head('Пример вопроса 2:')


def eric_example_2_answer():
    """Check «Ответ к примеру вопроса 2:»."""
    yield from eric_head('Ответ к примеру вопроса 2:')


def eric_proof():
    """Check «Источник(и):»."""
    yield from eric_head('Источник(и):')


def eric_authors_and_editors():
    """Check «Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):»."""
    yield from eric_head(
        'Автор(ы), редакторы и рецензенты (если есть) материалов источника(ов):')


def eric_prooflink():
    """Check «Ссылка(и) на источник(и):»."""
    yield from eric_head('Ссылка(и) на источник(и):')


# def eric_head_summary():
#     """Report, contains head data in all files or no.

#     Python >= 3.5 lists (and generators) concatenation
#     https://stackoverflow.com/a/35631185/5951529

#     Returns:
#         bool -- False if any error

#     """
#     eric_concat_head = [item for item in [*eric_package_description(),
#                                           *eric_training_process(),
#                                           *eric_example_1(),
#                                           *eric_example_1_answer(),
#                                           *eric_example_2(),
#                                           *eric_example_2_answer(),
#                                           *eric_proof(),
#                                           *eric_authors_and_editors(),
#                                           *eric_prooflink(),
#                                           *eric_package_link()]]

#     if not all(eric_concat_head):
#         pyfancy_error(
#             'One or more packages not contains one or more head data. Please, add correct head data to your package.')
#         return False
#     pyfancy_notice('All files contains correct head data')
#     return True
