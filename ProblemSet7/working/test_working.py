from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:26 AM to 11:20 PM") == "00:26 to 23:20"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"



    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM") == ValueError
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM") == ValueError

