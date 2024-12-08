x = input("camelCase: ")
print("snake_case: ", end="")
for i in x:
    if i in x.lower():
        print(i, end="")
    else:
        print("_", end="")
        print(i.lower(), end="")
print()
