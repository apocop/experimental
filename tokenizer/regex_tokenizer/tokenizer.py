import re
from .locales.en import tokenizer_rules


tokenizer_rules = tokenizer_rules
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
            # Create Conditions.
            initial_punctuation = re.match(tokenizer_rules.get('INITIAL_PUNCTUATION_TOKEN'), span, re.IGNORECASE)
            final_punctuation = re.match(tokenizer_rules.get('FINAL_PUNCTUATION_TOKEN'), span, re.IGNORECASE)
            all_punctuation = re.match(tokenizer_rules.get('ALL_PUNCTUATION_TOKEN'), span, re.IGNORECASE)
            currency_amount = re.match(tokenizer_rules.get('CURRENCY_AMOUNT_TOKEN'), span, re.IGNORECASE)

            #Intial Punctuation.
            if initial_punctuation:
                tokenize_group(initial_punctuation)
            # Final Punctuation.
            elif final_punctuation:
                tokenize_group(final_punctuation)
            # All Punctuation.
            elif all_punctuation:
                tokenize_group(all_punctuation)
            # Currency amount.
            elif currency_amount:
                tokenize_group(currency_amount)
            else:
                tokens.append(span)
    return tokens