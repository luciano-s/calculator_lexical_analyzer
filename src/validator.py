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
        self.validators = [
            Validator.is_number,
            Validator.is_plus_sign,
            Validator.is_minus_sign,
            Validator.is_multiplication_sign,
            Validator.is_division_sign,
            Validator.is_equals_sign,
        ]

    def validate_lexem(self, lexem: str) -> dict:
        try:
            return list(
                filter(
                    lambda x: x[lexem] != None,
                    [validator(lexem) for validator in self.validators],
                )
            ).pop()

        except:
            return {lexem: None}

    def validate_lexems(self, lexem_list: list) -> list:
        return [self.validate_lexem(lexem) for lexem in lexem_list]

    @classmethod
    def is_number(cls, value: str) -> dict:
        number_pattern = re.compile("([0-9]+|[0-9]+.[0-9]+)")
        check = lambda x: {x: "<NUMBER>"} if number_pattern.match(x) else {x: None}
        return check(value)

    @classmethod
    def is_plus_sign(cls, value: str) -> dict:
        plus_sign_pattern = re.compile("[+]")
        check = (
            lambda x: {x: "<PLUS_SIGN>"} if plus_sign_pattern.match(x) else {x: None}
        )
        return check(value)

    @classmethod
    def is_minus_sign(cls, value: str) -> dict:
        plus_sign_pattern = re.compile("-")
        check = (
            lambda x: {x: "<MINUS_SIGN>"} if plus_sign_pattern.match(x) else {x: None}
        )
        return check(value)

    @classmethod
    def is_multiplication_sign(cls, value: str) -> dict:
        multiplication_sign_pattern = re.compile("[*]")
        check = (
            lambda x: {x: "<MULTIPLICATION_SIGN>"}
            if multiplication_sign_pattern.match(x)
            else {x: None}
        )
        return check(value)

    @classmethod
    def is_division_sign(cls, value: str) -> dict:
        division_sign_pattern = re.compile("/")
        check = (
            lambda x: {x: "<DIVISION_SIGN>"}
            if division_sign_pattern.match(x)
            else {x: None}
        )
        return check(value)

    @classmethod
    def is_equals_sign(cls, value: str) -> dict:
        equals_sign_pattern = re.compile("=")
        check = (
            lambda x: {x: "<EQUALS_SIGN>"}
            if equals_sign_pattern.match(x)
            else {x: None}
        )
        return check(value)
