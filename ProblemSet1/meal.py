def main():
    x = input("What time is it? ")
    t = convert(x)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        print("Invalid Input")

def convert(time):
    [h, m] = time.split(":")
    out = float(int(h) + int(m)/60)
    return out


if __name__ == "__main__":
    main()
