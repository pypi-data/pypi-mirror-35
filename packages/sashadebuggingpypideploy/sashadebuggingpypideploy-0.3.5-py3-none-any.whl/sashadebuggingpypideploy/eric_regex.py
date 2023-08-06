# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 19:58:48
# @Last Modified time: 2018-08-24 08:13:46
"""Regex Checker.

Check, if regexes contains in each line of package for Eric room.

Do not check:
    1. lines before <body> and line with <body>,
    2. <!-- comments -->,
    3. lines, contains “'*-noerichek-'”,
    4. lines between <noerichek></noerichek>,
    5. lines, contains “^Тема:”
"""
import regex

import os

from bs4 import BeautifulSoup

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS
from erichek.eric_config import pyfancy_debug
from erichek.eric_config import pyfancy_error
from erichek.eric_config import pyfancy_notice

# Replacing
# Add missing dot
ADD_DOT = r'\1\5.\6'
# Remove extra dot
REMOVE_DOT = r'\1\5'

REGEX_DATA = True


def eric_initial_function():
    """Make list of packages lines.

    List, for which will make actions of this module.

    Yields:
        list -- list of questions without exceptions

    """
    for filename in ALL_TXT_IN_ERIC_ROOM_WITHOUT_SUBFOLDERS:

        global filename_without_path
        filename_without_path = os.path.basename(filename)
        # Open file:
        # https://stackoverflow.com/a/3277515/5951529
        # “with open” better, because file properly closed, even an exception:
        # https://stackoverflow.com/a/36860392/5951529
        with open(filename, encoding='utf-8') as unhandled_file:
            # File as string:
            # https://stackoverflow.com/a/16082963/5951529
            file_as_string = unhandled_file.read()
            # Remove before “<body>”, include “<body>”:
            # https://stackoverflow.com/a/16405619/5951529
            file_after_body = file_as_string.split('<body>', 1)[-1]
            # Remove all symbols between tags include tags:
            # https://stackoverflow.com/a/5598678/5951529
            # Support multiple tags:
            # https://stackoverflow.com/questions/5598524/5598678#comment17574202_5598678
            noerichek_soup = BeautifulSoup(file_after_body, 'lxml')
            [s.extract() for s in noerichek_soup('noerichek')]
            # Remove all tags and comments from file:
            # [NOTE] It remove and all commented lines from package:
            # https://stackoverflow.com/a/28162403/5951529
            soup_as_text = noerichek_soup.get_text()
            # Split multiline string to multiple lines:
            # https://stackoverflow.com/a/172454/5951529
            soup_text_as_list = soup_as_text.splitlines()
            # Remove blank list items:
            # https://stackoverflow.com/a/16099706/5951529
            noempty_list = list(filter(None, soup_text_as_list))
            # Remove list items, contains data, prohibiting Erichek:
            # https://stackoverflow.com/a/3416473/5951529
            # For multiple items:
            # https://stackoverflow.com/a/12666923/5951529
            global final_list
            final_list = [x for x in noempty_list if not (
                'Тема:' in x or '*-noerichek-' in x)]
            # “yield” continue function:
            # Lutz, 20.2.2
            yield final_list


def eric_all(regex_find, regex_essence):
    """Wrap “if all”.

    Check all elements of list, that contains «*»
    https://stackoverflow.com/a/44118151/5951529
    List comprehension: print incorrect list items
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    Check all list items by regex:
    https://ru.stackoverflow.com/a/867210/199934

    Arguments:
        regex_find {str} -- regex, that erichek find in each line
        regex_essence {str} -- essense, that erichek find
    """
    for final_list in eric_initial_function():
        # List comprehension, if list item contain regex.
        # For replacing “for/if/for” with additional variable “find_variable”, example:
        # for package_line in final_list:
        #     find_variable = regex.search(regex_find, package_line)
        #     if not find_variable:
        #         pyfancy_error("Error")
        # Lutz, 14.2.3
        entrance_good_list = [
            package_line for package_line in final_list if regex.search(
                regex_find,
                package_line) is None]
        if not entrance_good_list:
            pyfancy_debug(
                'All lines in ' +
                filename_without_path +
                ' contain ' +
                regex_essence)
        else:
            for package_line in entrance_good_list:
                pyfancy_error(
                    "This line not contain " +
                    regex_essence +
                    package_line +
                    " in " +
                    filename_without_path)
            global REGEX_DATA
            REGEX_DATA = False


def eric_any(regex_find, regex_essence):
    """Wrap “if not any”.

    If any question not contain regex, return False.
    https://www.programiz.com/python-programming/methods/built-in/any

    Arguments:
        regex_find {str} -- regex, that erichek find in each line
        regex_essence {str} -- essense, that erichek find

    Yields:
        list -- list of lines for each file

    """
    for final_list in eric_initial_function():
        # for testline in final_list:
        #     r = regex.search(regex_find, final_list)
        #     print("r", r)
        # print("final_list", final_list)
        entrance_bad_list = [
            package_line for package_line in final_list if regex.search(
                regex_find,
                package_line) is not None]
        # print("entrance_bad_list1", entrance_bad_list)
        if not entrance_bad_list:
            pyfancy_debug(
                filename_without_path +
                ' doesn\'t contain ' +
                regex_essence)
        else:
            yield entrance_bad_list


def eric_any_find(regex_find, regex_essence):
    """Check, that regex doesn't contains.

    Check, not replace.

    Arguments:
        regex_find {str} -- regex, that erichek find in each line
        regex_essence {str} -- essense, that erichek find
    """
    for entrance_bad_list in eric_any(regex_find, regex_essence):
        # print("entrance_bad_list", entrance_bad_list)
        for package_line in entrance_bad_list:
            # print("package_line", package_line)
            pyfancy_error("This line contain " + regex_essence + package_line +
                          " in " + filename_without_path)
            global REGEX_DATA
            REGEX_DATA = False


def eric_any_replace(regex_find, regex_essence, regex_replace):
    """Check regex and replace to right.

    Accept, if replacing in file needed.

    Arguments:
        regex_find {str} -- regex, that erichek find in each line
        regex_essence {str} -- essense, that erichek find
        regex_replace {str} -- regex for replacing
    """
    for entrance_bad_list in eric_any(regex_find, regex_essence):
        # print("entrance_bad_list", entrance_bad_list)
        for package_line in entrance_bad_list:
            # print("package_line", package_line)
            pyfancy_error("This line not contain dot in " + regex_essence + package_line +
                          " in " + filename_without_path)
            pyfancy_notice("If you get this message in local testing, Erichek automatically " + regex_essence +
                           "Else you get message in CI output, please, run Erichek locally, that fix the problem.")
            # Overwrite files via truncate():
            # https://stackoverflow.com/a/44137923/5951529
            # “r+” — for reading and writing:
            # https://stackoverflow.com/a/13248062/5951529
            # encoding='utf-8' required
            file = open(filename_without_path, 'r+', encoding='utf-8')
            data = file.read()
            file.seek(0)
            file.write(
                regex.sub(
                    regex_find,
                    regex_replace,
                    data,
                    # Multiline flag, that works start-of-line anchor:
                    # https://stackoverflow.com/a/17649039/5951529
                    flags=regex.M))
            file.truncate()
            file.close()
        global REGEX_DATA
        REGEX_DATA = False


def eric_answers():
    """Check, that answer exist in each line.

    https://regex101.com/r/VdSCgV/1/
    """
    eric_all(r'\*[^-]', 'asterisks: ')


def eric_proofs():
    """Check, that “*-proof-” exist in each line.

    https://regex101.com/r/VhZOOE/1/
    """
    eric_all(r'\*-proof-.', 'proofs: ')


def eric_wikipedia():
    """Check each line, that not contains links to Wikipedia or Commons.

    [description]
    """
    eric_any_find(r'wikipedia', 'link to Wikipedia: ')


def eric_add_question_dot():
    """Check and add final dot to question.

    https://regex101.com/r/SH9KBA/1
    """
    eric_any_replace(
        r'^(((http.+\.(apng|bmp|gif|jpeg|jpg|png) )?)[^.*]+\.)([^.*]+)(\*)',
        'add dot to question. ',
        ADD_DOT)


def eric_add_comment_dot():
    """Check and add final dot to comment.

    https://regex101.com/r/SH9KBA/2
    """
    eric_any_replace(
        r'(\*-info-((http.+\.(apng|bmp|gif|jpeg|jpg|png) )?)[^.*]+\.)([^.*]+)(\*)',
        'add dot to comment. ',
        ADD_DOT)


def eric_remove_question_dot():
    """Check and remove extra dot in question.

    https://regex101.com/r/3ktrce/4
    """
    eric_any_replace(
        r'^(((http.+\.(apng|bmp|gif|jpeg|jpg|png) )?)[^.*]+?)\.(\*)',
        'remove dot from question. ',
        REMOVE_DOT)


def eric_remove_comment_dot():
    """Check and remove extra dot in comment.

    https://regex101.com/r/M5EKdY/4
    """
    eric_any_replace(
        r'(\*-info-((http.+\.(apng|bmp|gif|jpeg|jpg|png) )?)[^.]+?)\.(\*-)',
        'remove dot from comment. ',
        REMOVE_DOT)


def eric_regex_summary():
    """Report, contains regexes in all files or no."""
    eric_answers()
    eric_proofs()
    eric_wikipedia()
    eric_add_question_dot()
    eric_add_comment_dot()
    eric_remove_question_dot()
    eric_remove_comment_dot()
    if REGEX_DATA:
        pyfancy_notice(
            "All files correspond to the rules of regular expressions")

    else:
        pyfancy_error(
            "One or more your files correspond to the rules of regular expressions. Please, correct your package(s).")
