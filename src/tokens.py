
from src.validator import Validator


class Tokens:

    def split_token(self, input: str) -> list:
        token_list = []
        validator = Validator()
        token = ""
        col = 1
        for c in input:
            token_type = validator.validate_lexem(c)
            if token_type[c] == "<NUMBER>" or c == ".":
                token += c
            else:
                if token != "":
                    col_i = col-len(token)
                    token_list.append(
                        (col_i, col, validator.validate_lexem(token)))
                    token = ""
                token_list.append((col, col+1, token_type))
            col += 1
        if token != "":
            col_i = col-len(token)
            token_list.append((col_i, col, validator.validate_lexem(token)))
        # print(token_list)
        return token_list

    def split_tokens(self, inputs: list) -> list:
        return [self.split_token(in_) for in_ in inputs]
