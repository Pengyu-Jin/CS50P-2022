from plates import is_valid

def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("cs,5") == False
    assert is_valid("cs50p2") == False
    assert is_valid("csnbnbnb") == False
    assert is_valid("csnb") == True
    assert is_valid("H") == False
    assert is_valid("505") == False
