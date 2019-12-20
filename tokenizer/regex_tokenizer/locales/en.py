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
    return re.compile(BOS + rule + EOS, re.IGNORECASE)

def group(group):
    # Creates regex groups.
    return OPEN_GROUP + group + CLOSE_GROUP

# Basic Characters.
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
CURRENCY_SYMBOL = '[$£¥]'
ZERO_OR_ONE = '?'

# Character Regex Groups.
ALPHA_GROUP = group(ALPHA)
INITIAL_PUNCTUATION_GROUP = group(INITIAL_PUNCTUATION)
FINAL_PUNCTUATION_GROUP = group(FINAL_PUNCTUATION + PLUS)
CURRENCY_SYMBOL_GROUP = group(CURRENCY_SYMBOL)
CURRENCY_GROUP = group(DIGITS + PLUS + PERIOD + ZERO_OR_ONE + DIGITS + '{,2}')

# Grammar rules.
INITIAL_PUNCTUATION_TOKEN = INITIAL_PUNCTUATION_GROUP + ALPHA_GROUP
FINAL_PUNCTUATION_TOKEN = ALPHA_GROUP + FINAL_PUNCTUATION_GROUP
ALL_PUNCTUATION_TOKEN = OPEN_GROUP + FINAL_PUNCTUATION + CLOSE_GROUP + FINAL_PUNCTUATION_GROUP
CURRENCY_AMOUNT_TOKEN = CURRENCY_SYMBOL_GROUP + CURRENCY_GROUP

rules_to_export = {
    'INITIAL_PUNCTUATION_TOKEN' : INITIAL_PUNCTUATION_TOKEN,
    'FINAL_PUNCTUATION_TOKEN' : FINAL_PUNCTUATION_TOKEN,
    'ALL_PUNCTUATION_TOKEN' : ALL_PUNCTUATION_TOKEN,
    'CURRENCY_AMOUNT_TOKEN' : CURRENCY_AMOUNT_TOKEN,
}

# Rules with word boundaries.
tokenizer_rules = {k:compile_rule(v) for (k,v) in rules_to_export.items()}