from cipher_zh2387 import cipher_zh2387

def test_single_cipher():
    t = 'All about us'
    s = 3
    expected = 'Doo derxw xv'
    actual = cipher_zh2387.cipher(t,s)
    assert actual == expected