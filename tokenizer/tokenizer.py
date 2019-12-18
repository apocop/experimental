"""
A tokenizer example for English text.
"""

class Token(object):
    """A token object."""
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'Token: {self.token}'

    def __len__(self):
        return len(self.token)


class Tokenizer(object):
    "Tokenizes a string and returns a Document of Tokens."

    def __init__(self):

        self.tokens = []
        self.token_cache = []

        # English specific customizations.
        self.inital_punctuation = ('\'', '"')
        self.final_punctuation = ('\'', '"', '!', '?', '.', ',')
        self.token_exceptions = {
            'don\'t' : ('do', 'n\'t'),
            'doen\'t': ('does', 'n\'t'),
            'haven\'t': ('have', 'n\'t'),
            ':)': (':)',),
            ':(': (':(',),
        }

    def add_token(self, approved_token):
        """Add an approved token to the final token list."""
        self.tokens.append(Token(approved_token))

    def tokenize(self, text):
        """Go through the tokenization pipeline to produce tokens."""
        for preprocessed_token in text.split():
            if preprocessed_token in self.token_exceptions:
                self.add_exceptions(preprocessed_token)
            else:
                preprocessed_token = self.split_prefix(preprocessed_token)
                preprocessed_token = self.split_suffix(preprocessed_token)

                if preprocessed_token:
                    self.add_token(preprocessed_token)

        return Document(self.tokens, text)


    def add_exceptions(self, preprocessed_token):
        """Check to see if the token has a hard coded tokenization."""
        for token in self.token_exceptions.get(preprocessed_token):
            self.add_token(token)

    def split_prefix(self, preprocessed_token):
        "Split initial punctuation."
        if preprocessed_token[0] in self.inital_punctuation:
            self.add_token(preprocessed_token[0])
            preprocessed_token = self.split_prefix(preprocessed_token[1:])
            return preprocessed_token
        else:
            return preprocessed_token

    def split_suffix(self, preprocessed_token):
        "Stem final punctuation."

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
                else:
                    self.add_token(token)
            return None
        else:
            return preprocessed_token

    def add_to_token_cache(self, token):
        self.token_cache.append(token)

    def pop_from_token_cache(self):
        return self.token_cache.pop()


class Document(object):
    """Container Object for Tokens."""
 
    def __init__(self, tokens, text):
        self.tokens = tuple(tokens)
        self.text = text

    def __len__(self):
        return len(self.tokens)

    def __iter__(self):
        return iter(self.tokens)


# Temporary Tests.
s = """
These aren’t trivial numbers.
Compared to placebo, 20 more people were dying every year when taking these
two supplements. Over the four years of the trial, that equates to 80 more
deaths. As the authors wrote at the time, “The present findings provide
ample grounds to discourage use of supplemental beta-carotene and the
combination of beta-carotene and vitamin A.”
"""
s = 'I love you. :) Not!!! :('

tokenizer = Tokenizer()
processed_text = tokenizer.tokenize(s)

print(f'Number of tokens: {len(processed_text)}')
for token in processed_text:
    print(token)