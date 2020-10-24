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
            "<EQUALS_SIGN>",
        ]
        self.validators = [Validator.is_number]

    def validate_lexem(self, lexem: str) -> dict:
        return list(
            filter(
                lambda x: x.keys != None,
                [token_checker(lexem) for token_checker in self.validators],
            )
        ).pop()

    def validate_lexems(self, lexem_list: list) -> list:
        return [self.validate_lexem(lexem) for lexem in lexem_list]

    @classmethod
    def is_number(cls, value):
        number_pattern = re.compile("([0-9]+|[0-9]+.[0-9]+)")
        check = lambda x: {x: "<NUMBER>"} if number_pattern.match(x) else {x: None}
        return check(value)