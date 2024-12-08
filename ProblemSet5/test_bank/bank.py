def main():
    x = input("Greeting: ")
    s = x.lstrip()
    o = value(s)
    print(f"${o}")

def value(greeting):
    if greeting[:5].title() == "Hello":
        return 0
    elif greeting[0].title() == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

