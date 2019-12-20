import re
from .locales.en import tokenizer_rules


tokenizer_rules = tokenizer_rules
exceptions = {
    "don't" : ['do', 'not']
    }


tokens = []

def tokenize(text):
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

            # Intial Punctuation.
            if initial_punctuation:
                tokenize(initial_punctuation.group(1))
                tokenize(initial_punctuation.group(2))
            # Final Punctuation.
            elif final_punctuation:
                tokenize(final_punctuation.group(1))
                tokenize(final_punctuation.group(2))
            # All Punctuation.
            elif all_punctuation:
                tokenize(all_punctuation.group(1))
                tokenize(all_punctuation.group(2))
            # Currency amount.
            elif currency_amount:
                tokenize(currency_amount.group(1))
                tokenize(currency_amount.group(2))
            else:
                tokens.append(span)
    return tokens