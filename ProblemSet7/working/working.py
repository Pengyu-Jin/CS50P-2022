import re


def main():
    print(convert(input("Hours: ")))




def convert(s):
    match = re.search(r"^([1-9]|10|11|12)( |:[0-5][0-9] )(A|P)M to ([1-9]|10|11|12)( |:[0-5][0-9] )(A|P)M$", s)
    if not match:
        raise ValueError("ValueError")

    if match:
        if match.group(3) == "A":
            a_h = match.group(1)
            a_m = match.group(2)
            p_h = match.group(4)
            p_m = match.group(5)
        if match.group(3) == "P":
            p_h = match.group(1)
            p_m = match.group(2)
            a_h = match.group(4)
            a_m = match.group(5)
        if a_h == "12":
            a_h = "00"
        elif a_h == "11" or a_h == "10":
            pass
        else:
            a_h = "0" + a_h

        if a_m == " ":
            a_m = "00"
        else:
            a_m = a_m[1:3]

        if p_m == " ":
            p_m = "00"
        else:
            p_m = p_m[1:3]

        if p_h == "12":
            pass
        else:
            p_h = int(p_h) + 12

        if match.group(3) == "A":
            return f"{a_h}:{a_m} to {p_h}:{p_m}"
        if match.group(3) == "P":
            return f"{p_h}:{p_m} to {a_h}:{a_m}"


if __name__ == "__main__":
    main()
