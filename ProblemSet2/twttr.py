x = input("Input:")
print("Output:", end="")
for i in x:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("", end="")
    else:
        print(i, end="")
print()
