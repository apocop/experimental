import re



sample =  """"I don't like that dog", he remarked.""" 
sample = "Apple is looking at buying U.K. startup for $1 billion."

# sample = """
# These aren’t trivial numbers.
# Compared to placebo, 20 more people were dying every year when taking these
# two supplements. Over the four years of the trial, that equates to 80 more
# deaths. As the authors wrote at the time, “The present findings provide
# ample grounds to discourage use of supplemental beta-carotene and the
# combination of beta-carotene and vitamin A.”
# """
# sample = 'I love you. :) Not!!! :('

# sample = "U.K."


alpha = '[A-Z]'
digits = '[0-9]'
inital_punctuation = '[\'"]'
final_punctuation = '[\',!?":.]'
currency_symbol = '[$£¥]'
boundary = '\B'


conditions = {
    'inital_punctuation' : f'{boundary}({inital_punctuation})({alpha}+){boundary}',
    'final_punctuation' : f'{boundary}({alpha}+)({final_punctuation}+){boundary}',
    'all_punctuation' : f'{boundary}({final_punctuation})({final_punctuation}+){boundary}',
    'currency_amount' : f'({currency_symbol})({digits}+\.?{digits}*)',
}

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
            initial_punctuation = re.match(conditions.get('inital_punctuation'), span, re.IGNORECASE)
            final_punctuation = re.match(conditions.get('final_punctuation'), span, re.IGNORECASE)
            all_punctuation = re.match(conditions.get('all_punctuation'), span, re.IGNORECASE)
            currency_amount = re.match(conditions.get('currency_amount'), span, re.IGNORECASE)

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


tokens = tokenize(sample)
for token in tokens:
    print("Token", token)