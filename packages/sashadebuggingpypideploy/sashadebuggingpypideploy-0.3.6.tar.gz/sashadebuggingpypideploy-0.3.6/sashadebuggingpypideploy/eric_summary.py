"""Docstring."""
from erichek.eric_config import pyfancy_error
from erichek.eric_config import pyfancy_notice
from erichek.eric_config import pyfancy_warning

import erichek.eric_head as head
import erichek.eric_regex as regex

from erichek.eric_body import eric_body_function
from erichek.eric_encoding import eric_encoding_function
from erichek.eric_eyo import eric_eyo


def eric_warning_exit_0(failed_object):
    """Docstring."""
    pyfancy_warning(
        "Your " +
        failed_object +
        " errors will automatically fixed.")
    return True


def eric_error_exit_1(failed_object):
    """Docstring."""
    pyfancy_error(
        "Not all files contain " +
        failed_object +
        " . You need to fix your package(s).")
    return False


def eric_summary_initial(summary_module, error_or_warning, failed_object):
    """Report, contains <body> in all files or no.

    [TIP] “if not all()” works as “if False in”.
    [TIP] That doesn't print “Это фиаско!” in any case, I need:
    Pass as variable — “eric_summary_initial(eric_warning_exit_0)”, not “eric_summary_initial(eric_warning_exit_0())”
    Call as function — “error_or_warning()”, not “error_or_warning”
    """
    if not all([item for item in summary_module]):
        return error_or_warning(failed_object)
    pyfancy_notice("All files contain " + failed_object)
    return True


def eric_encoding_summary():
    """Docstring."""
    return eric_summary_initial(
        eric_encoding_function(), eric_warning_exit_0, 'UTF-8 encoding')


def eric_body_summary():
    """Docstring."""
    return eric_summary_initial(
        eric_body_function(), eric_error_exit_1, 'body')


def eric_eyo_summary():
    """Docstring."""
    return eric_summary_initial(
        eric_eyo(), eric_warning_exit_0, 'eyo')


def eric_head_summary():
    """Docstring."""
    return eric_summary_initial([*head.eric_package_description(),
                                 *head.eric_training_process(),
                                 *head.eric_example_1(),
                                 *head.eric_example_1_answer(),
                                 *head.eric_example_2(),
                                 *head.eric_example_2_answer(),
                                 *head.eric_proof(),
                                 *head.eric_authors_and_editors(),
                                 *head.eric_prooflink(),
                                 *head.eric_package_link()],
                                eric_error_exit_1,
                                'head data')


def eric_regex_summary():
    """Docstring."""
    return eric_summary_initial([*regex.eric_answers(),
                                 *regex.eric_proofs(),
                                 *regex.eric_wikipedia(),
                                 *regex.eric_add_question_dot(),
                                 *regex.eric_add_comment_dot(),
                                 *regex.eric_remove_question_dot(),
                                 *regex.eric_remove_comment_dot()],
                                eric_error_exit_1,
                                'regex data')
