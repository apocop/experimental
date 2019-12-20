import re
from .locales.en import tokenizer_rules


rules = tokenizer_rules
exceptions = {
    "don't" : ['do', 'not']
    }

tokens = []

def tokenize(text):

    def tokenize_group(match):
        "Tokenize two groups from match object."
        tokenize(match.group(1))
        tokenize(match.group(2))

    for span in text.split():
        # Exceptions.
        if span in exceptions:
            for token in exceptions.get(span):
                tokenize(token)
        else:
            for rule in rules:
                match = re.match(rules.get(rule), span)
                if match:
                    tokenize_group(match)
                    break
                else:
                    if rule == list(rules)[-1]:
                        tokens.append(span)
    return tokens