import re

sample =  """"I don't like that dog!!!", he remarked.""" 

alpha = '[A-Z]'
inital_punctuation = '[\'"]'
final_punctuation = '[\',!?"]'

conditions = {
    'inital_punctuation' : f'({inital_punctuation})({alpha}+)',
    'final_punctuation' : f'({alpha}+)({final_punctuation}+)',
    'all_punctuation' : f'({final_punctuation})({final_punctuation}+)',
}


tokens = []

def tokenize(text):

    exceptions = {
    "don't" : ['do', 'not']
    }

    for span in text.split(' '):

        # Exceptions.
        if span in exceptions:
            for token in exceptions.get(span):
                tokenize(token)

        else:
            # Create Conditions.
            initial_punctuation = re.match(conditions.get('inital_punctuation'), span, re.IGNORECASE)
            final_punctuation = re.match(conditions.get('final_punctuation'), span, re.IGNORECASE)
            all_punctuation = re.match(conditions.get('all_punctuation'), span, re.IGNORECASE)

            # Intial Punctuation.
            if initial_punctuation:
                g1, g2 = initial_punctuation.group(1), initial_punctuation.group(2)
                tokenize(g1)
                tokenize(g2)
            # Final Punctuation.
            elif final_punctuation:
                g1, g2 = final_punctuation.group(1), final_punctuation.group(2)
                tokenize(g1)
                tokenize(g2)
            # All Punctuation.
            elif all_punctuation:
                g1, g2 = all_punctuation.group(1), all_punctuation.group(2)
                tokenize(g1)
                tokenize(g2)
            else:
                tokens.append(span)
    return tokens


tokens = tokenize(sample)
for token in tokens:
    print("Token", token)