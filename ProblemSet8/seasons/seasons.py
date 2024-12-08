import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    birth = input("Date of Birth: ")
    minutes = sub_date(birth)
    print(convert_to_text(minutes))

def sub_date(birth):
    try:
        d = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    # The result of subtracting one date object from another is a timedelta object
    sub = today - d
    return round(sub.total_seconds()/60)

def convert_to_text(num):
    return f"{p.number_to_words(num, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
