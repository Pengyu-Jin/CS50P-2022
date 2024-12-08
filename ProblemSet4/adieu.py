import inflect

p = inflect.engine()
namels = []
try:
    while True:
        x = input()
        namels.append(x)
except EOFError:
    print("Adieu, adieu, to " + p.join(namels))

