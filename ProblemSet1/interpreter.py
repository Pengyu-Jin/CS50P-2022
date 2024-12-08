x = input("Expression: ")
[x, y, z] = x.split(" ")
if y == "/" and z == "0":
    print("Zero cannot be a divisor")
elif y == "+":
    out = float(int(x) + int(z))
    print(f"{out:.1f}")
elif y == "-":
    out = float(int(x) - int(z))
    print(f"{out:.1f}")
elif y == "*":
    out = float(int(x) * int(z))
    print(f"{out:.1f}")
else:
    out = float(int(x) / int(z))
    print(f"{out:.1f}")

