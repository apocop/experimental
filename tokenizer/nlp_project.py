from regex_tokenizer.tokenizer import tokenize


# sample =  """"I don't like that dog", he remarked.""" 
# sample = "Apple is looking at buying U.K. startup for $1 billion."

# sample = """
# These aren’t trivial numbers.
# Compared to placebo, 20 more people were dying every year when taking these
# two supplements. Over the four years of the trial, that equates to 80 more
# deaths. As the authors wrote at the time, “The present findings provide
# ample grounds to discourage use of supplemental beta-carotene and the
# combination of beta-carotene and vitamin A.”
# """
sample = 'I love you. :) Not!!! :('

# sample = "U.K."



tokens = tokenize(sample)
for token in tokens:
    print("Token", token)