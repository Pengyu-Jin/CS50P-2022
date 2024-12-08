
from project import formatted_title


def test_formatted_title():
    input_title1 = "Hello"
    expected_output1 = (
        "+-------+\n"
        "| Hello |\n"
        "+-------+"
    )
    assert formatted_title(input_title1) == expected_output1

    input_title2 = "Hello\nWorld"
    expected_output2 = (
            "+-------+\n"
            "| Hello |\n"
            "| World |\n"
            "+-------+"
        )
    assert formatted_title(input_title2) == expected_output2

    input_title3 = "   Hello   "
    expected_output3 = (
        "+-------+\n"
        "| Hello |\n"
        "+-------+"
    )
    assert formatted_title(input_title3) == expected_output3

    