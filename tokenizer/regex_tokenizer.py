import re

sample =  """"I don't like that dog", he remarked.""" 

alpha = '[A-Z]'
inital_punctuation = '[\'"]'
final_punctuation = '[]'

conditions = {
    'inital_punctuation' : f'({inital_punctuation})({alpha}*)'
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
            # Intial Punctuation.
            has_initial_punctuation = re.match(conditions.get('inital_punctuation'), span, re.IGNORECASE)
            if has_initial_punctuation:
                print(has_initial_punctuation.group(0))
            # Final Puctuation
            elif re.match('{alpha}{final_punctuation}*', span, re.IGNORECASE):
                pass
            else:
                tokens.append(span)

    

    return tokens


tokens = tokenize(sample)
for token in tokens:
    print(token)