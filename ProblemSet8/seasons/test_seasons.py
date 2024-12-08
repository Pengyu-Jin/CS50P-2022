from ProblemSet8.seasons.seasons import sub_date
import pytest

def test_sub_date():
    sub_date("2023-11-26") == "five hundred twenty-seven thousand forty minutes"

    with pytest.raises(SystemExit):
        sub_date("xxxx")
