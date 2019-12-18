class Token(object):

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'Token: {self.token}'


class Tokenizer(object):

    def __init__(self):

        self.tokens = []
        self.inital_punctuation = ['\'', '"']
        self.final_punctuation = ['\'', '"', '!', '?', '!', '/', '\\', '.', ',']
        self.token_exceptions = {
            'don\'t' : ('do', 'n\'t'),
            'doen\'t': ('does', 'n\'t'),
            'haven\'t': ('have', 'n\'t'),
            ':)': (':)',),
        }

        self.token_cache = []

    def add_token(self, approved_token):
        self.tokens.append(Token(approved_token))

    def tokenize(self, text):

        for preprocessed_token in text.split():

            if preprocessed_token in self.token_exceptions:
                self.add_exceptions(preprocessed_token)
                continue

            preprocessed_token = self.split_prefix(preprocessed_token)
            preprocessed_token = self.split_suffix(preprocessed_token)

            if preprocessed_token:
                self.add_token(preprocessed_token)



        return Document(self.tokens)


    def add_exceptions(self, preprocessed_token):
        """Check to see if the token has a hard coded tokenization."""
        for token in self.token_exceptions.get(preprocessed_token):
            self.add_token(token)


    def split_prefix(self, preprocessed_token):
        if preprocessed_token[0] in self.inital_punctuation:
            self.add_token(preprocessed_token[0])
            preprocessed_token = self.split_prefix(preprocessed_token[1:])
            return preprocessed_token
        else:
            return preprocessed_token

    def split_suffix(self, preprocessed_token):

        suffix = preprocessed_token[-1]

        if suffix in self.final_punctuation:

            split_token = preprocessed_token[:-1]

            self.add_to_token_cache(suffix)

            if split_token[-1] in self.final_punctuation:
                self.split_suffix(split_token)
            else:
                self.add_to_token_cache(split_token)


            for i in range(0, len(self.token_cache)):

                token = self.pop_from_token_cache()

                if preprocessed_token in self.token_exceptions:
                    self.add_exceptions(preprocessed_token)
                    continue
            
                self.add_token(token)

            # self.clear_token_cache()

            return None


        else:
            return preprocessed_token

    def add_to_token_cache(self, token):
        self.token_cache.append(token)

    def pop_from_token_cache(self):
        return self.token_cache.pop()

    def clear_token_cache(self):
        self.token_cache = []

class Document(object):
 
    def __init__(self, tokens):
        self.tokens = tokens
        # self.tokens = set(tokens)

    def __len__(self):
        return len(self.tokens)



s = "Apple is looking at buying U.K. startup for $ 1billion."
s = '"Apple'
s = "'I don't have an apple.' Apple is looking at buying U.K. startup for $1 billion."
s = "'I don't have an apple.'"
s = "'I don't have an apple,' he said."

s = """
These aren’t trivial numbers. Compared to placebo, 20 more people were dying every year when taking these two supplements. Over the four years of the trial, that equates to 80 more deaths. As the authors wrote at the time, “The present findings provide ample grounds to discourage use of supplemental beta-carotene and the combination of beta-carotene and vitamin A.”
"""
s = 'I love you. :) Not!!!'
tokenizer = Tokenizer()
processed_text = tokenizer.tokenize(s)


print(len(processed_text))
for x in range(0, len(processed_text.tokens)):
    print(processed_text.tokens[x])