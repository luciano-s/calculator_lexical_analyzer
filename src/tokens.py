import sys
sys.path.append(
    "calculator_lexical_analyzer/src"
)
from validator import Validator


class Tokens:

    def split_tokens(self, input: str) -> list:
        token_list = []
        validator = Validator()
        token = ""
        for c in input:
            token_type = validator.validate_lexem(c)
            if token_type[c] == "<NUMBER>" or c == ".":
                token += c
            else:
                print(token)
                if token != "":
                    token_list.append(validator.validate_lexem(token))
                    token = ""
                token_list.append(token_type)
        if token != "":
            token_list.append(validator.validate_lexem(token))
            token = ""
        return token_list

    def split_tokens(self, inputs: list) -> list:
        return [self.split_tokens(in_) for in_ in inputs]
