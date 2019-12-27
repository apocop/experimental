"""
English Tokenizer Grammar
This grammar defines a series of rules multi-token English strings and
groupings of how the tokenizer should split them.
Each rule can have only exactly two groupings that must account for every
character in the string.

Examples:

1. $4 ⟶ $ 4
2. "I ⟶ " I
3. said," ⟶ said , "
"""

import re

def compile_rule(rule):
    """Return a case insensitive rule matching and entire string."""
    return re.compile(BOS + rule + EOS, re.IGNORECASE)

def create_group(expression):
    """ Returns regular expression groups."""
    return OPEN_GROUP + expression + CLOSE_GROUP

# Basic characters and sets.
ALPHA = '[A-Z]+'
DIGITS = '[0-9]'
BOS = '^'
EOS = '$'
PLUS = '+'
STAR = "*"
PERIOD = r'\.'
OPEN_GROUP = '('
CLOSE_GROUP = ')'
INITIAL_PUNCTUATION = '[\'"]'
FINAL_PUNCTUATION = '[\',!?":.]'
CURRENCY_SYMBOL = '[$£¥€]'
ZERO_OR_ONE = '?'

# Regular expression groups.
ALPHA_GROUP = create_group(ALPHA)
INITIAL_PUNCTUATION_GROUP = create_group(INITIAL_PUNCTUATION)
FINAL_PUNCTUATION_GROUP = create_group(FINAL_PUNCTUATION + PLUS)
FINAL_PUNCTUATION_STAR_GROUP = create_group(FINAL_PUNCTUATION + STAR)
CURRENCY_SYMBOL_GROUP = create_group(CURRENCY_SYMBOL)
CURRENCY_GROUP = create_group(DIGITS + PLUS + PERIOD + ZERO_OR_ONE + DIGITS + '{,2}')
ALPHA_PUNCTUATION_GROUP = create_group(ALPHA + FINAL_PUNCTUATION + STAR)

# Grammar rules.
INITIAL_PUNCTUATION_TOKEN = INITIAL_PUNCTUATION_GROUP + ALPHA_PUNCTUATION_GROUP
FINAL_PUNCTUATION_TOKEN = ALPHA_GROUP + FINAL_PUNCTUATION_GROUP
ALL_PUNCTUATION_TOKEN = OPEN_GROUP + FINAL_PUNCTUATION + CLOSE_GROUP + FINAL_PUNCTUATION_GROUP
CURRENCY_AMOUNT_TOKEN = CURRENCY_SYMBOL_GROUP + CURRENCY_GROUP + FINAL_PUNCTUATION_STAR_GROUP

RULES_TO_EXPORT = {
    'initial_punctuation_token' : INITIAL_PUNCTUATION_TOKEN,
    'final_punctuation_token' : FINAL_PUNCTUATION_TOKEN,
    'all_punctuation_token' : ALL_PUNCTUATION_TOKEN,
    'currency_amount_token' : CURRENCY_AMOUNT_TOKEN,
}

# Compiled rules with word boundaries.
RULES = {key:compile_rule(value) for (key, value) in RULES_TO_EXPORT.items()}