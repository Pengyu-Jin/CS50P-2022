def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
    return True

if __name__ == "__main__":
    main()
