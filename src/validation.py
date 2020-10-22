import re


class Validation:

    def __init__(self, valid_lexems:list, tokens:list):
        self.valid_tokens = Validation.build_lexems(valid_lexems, tokens)

    
    @classmethod
    def build_lexems(cls, lexems:list, tokens:list):
        valid_tokens_dict = {}

        for valid_token in zip(lexems, tokens):
            valid_tokens_dict[valid_token[0]] = valid_token[1]

    @classmethod
    def tokenize(cls, expression:str):
        pass

    @classmethod
    def analyze_expressions(cls, expressions:list):
        pass
         
        
