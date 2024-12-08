x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x = x.strip()
x_new = ""
for i in x:
    x_new = x_new +  i.lower()
if x_new == "42" or x_new == "forty-two" or x_new == "forty two":
    print("Yes")
else:
    print("No")
