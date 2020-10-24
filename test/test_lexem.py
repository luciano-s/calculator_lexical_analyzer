import re
import sys

sys.path.append(
    "/home/luciano/Documents/unesp/4_2_ano/compiladores/calculator_lexical_analyzer/src"
)
import pytest
from validator import Validator


def test_number_lexem():
    """
    Test if it can validate a number
    """
    lexems = ["1.97", "1", "1.0", "37", "0.58"]
    validator = Validator()
    assert validator.validate_lexems(lexems) == [
        {"1.97": "<NUMBER>"},
        {"1": "<NUMBER>"},
        {"1.0": "<NUMBER>"},
        {"37": "<NUMBER>"},
        {"0.58": "<NUMBER>"},
    ]
