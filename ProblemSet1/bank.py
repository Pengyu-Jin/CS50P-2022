x = input("Greeting: ")
s = x.lstrip()
if s[:5].title() == "Hello":
    print("$0")
elif s[0].title() == "H":
    print("$20")
else:
    print("$100")
