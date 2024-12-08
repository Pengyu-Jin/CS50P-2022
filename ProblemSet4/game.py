import random

while True:
    try:
        n = int(input("Level: "))
        goal = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        g = int(input("Guess: "))
        if g <= 0:
            continue
        elif g < goal:
            print("Too small!")
        elif g > goal:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

# the following program did't reject non-positive guess, just pass, understand the difference
#
# while True:
#     try:
#         g = int(input("Guess: "))
#         if 0 < g < goal:
#             print("Too small!")
#         elif g > goal:
#             print("Too large!")
#         elif g < 0:
#             pass
#         else:
#             print("Just right!")
#             break
#     except ValueError:
#         pass

