import re
import sys
import pytest

# python won't let me import Validator if I don't add the path to it
sys.path.append(
    "calculator_lexical_analyzer/src"
)

from validator import Validator


def test_number_lexem():
    """
    Test if it can validate a number
    """

    lexems = ["1.97", "1", "1.0", "37", "0.58", '.5', '.', '1.', '[0-9]', '(([0-9]+)|([0-9]+.[0-9]+))']

    validator = Validator()
    assert validator.validate_lexems(lexems) == [
        {"1.97": "<NUMBER>"},
        {"1": "<NUMBER>"},
        {"1.0": "<NUMBER>"},
        {"37": "<NUMBER>"},
        {"0.58": "<NUMBER>"},
        {".5": None},
        {'.':None},
        {'1.':None},
        {'[0-9]':None},
        {'(([0-9]+)|([0-9]+.[0-9]+))': None}

    ]


def test_sign_lexem():
    """
    Test if it can validate a sign lexem, +, -, * and /
    """
    lexems = ["+", "-", "*", "/", "=", "batata", "#", "@", "!", "_", "$", "%"]
    validator = Validator()
    assert validator.validate_lexems(lexems) == [
        {"+": "<PLUS_SIGN>"},
        {"-": "<MINUS_SIGN>"},
        {"*": "<MULTIPLICATION_SIGN>"},
        {"/": "<DIVISION_SIGN>"},
        {"=":"<EQUALS_SIGN>"},
        {"batata":None},
        {"#":None},
        {"@":None},
        {"!":None},
        {"_":None},
        {"$":None},
        {"%":None},
    ]