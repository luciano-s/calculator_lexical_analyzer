import re


class Validator:
    def __init__(self):
        self.token_types = [
            "<NUMBER>",
            "<OPEN_PARENTHESIS>",
            "<CLOSE_PARENTHESIS>",
            "<PLUS_SIGN>",
            "<MINUS_SIGN>",
            "<MULTIPLICATION_SIGN>",
            "<DIVISION_SIGN>",
            "<DOT>",
            "<EQUALS_SIGN>"
        ]

    @classmethod
    def validate_lexem(lexem: str) -> bool:
        pass

    @classmethod
    def validate_lexems(lexem_list: list) -> list:
        pass
