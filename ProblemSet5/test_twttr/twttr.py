def main():
    x = input("Input: ")
    out = shorten(x)
    print("Output:", out)

def shorten(s):
    new_s = ""
    for i in s:
        if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new_s += i
    return new_s

if __name__ == "__main__":
    main()
