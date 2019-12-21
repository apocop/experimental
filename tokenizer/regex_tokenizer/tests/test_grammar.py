from RegTokenizer.grammars import en

tokenizer_rules = en.rules

def test_inital_punctuation_rule():
    assert tokenizer_rules['INITIAL_PUNCTUATION_TOKEN'].pattern == """^([\'"])([A-Z]+[\',!?":.]*)$"""

def test_final_punctuation_rule():
    assert tokenizer_rules['FINAL_PUNCTUATION_TOKEN'].pattern == """^([A-Z]+)([',!?":.]+)$"""

def test_all_punctuation_rule():
    assert tokenizer_rules['ALL_PUNCTUATION_TOKEN'].pattern == """^([',!?":.])([',!?":.]+)$"""

def test_punctuation_rule():
    assert tokenizer_rules['CURRENCY_AMOUNT_TOKEN'].pattern == r"""^([$£¥])([0-9]+\.?[0-9]{,2})$"""