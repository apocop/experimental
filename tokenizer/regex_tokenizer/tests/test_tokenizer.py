from RegTokenizer import tokenizer

tokenizer = tokenizer.tokenize

def test_tokenizer():
    assert tokenizer('hi') == ['hi']