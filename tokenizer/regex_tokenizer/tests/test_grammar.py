from locales import en

def test_regex_rules():
    tokenizer_rules = en.tokenizer_rules
    assert tokenizer_rules['INITIAL_PUNCTUATION_TOKEN'] == r"""^(['"])([A-Z]+)$"""
    assert tokenizer_rules['FINAL_PUNCTUATION_TOKEN'] == r"""^([A-Z]+)([',!?":.]+)$"""
    assert tokenizer_rules['ALL_PUNCTUATION_TOKEN'] == r"""^([',!?":.])([',!?":.]+)$"""
    assert tokenizer_rules['CURRENCY_AMOUNT_TOKEN'] == r"""^([$£¥])([0-9]+\.?[0-9]{,2})$"""
