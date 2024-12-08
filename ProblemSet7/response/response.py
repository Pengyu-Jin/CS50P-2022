from validator_collection import validators, errors
import sys

def validate(email):
    try:
        if validators.email(email, allow_empty = False):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


def main():
    print(validate(input("What's your email address? ")))

if __name__ == "__main__":
    main()
