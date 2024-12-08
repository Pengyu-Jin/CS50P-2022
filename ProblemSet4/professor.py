import random

def main():
    score = 10
    n = get_level()
    j = 0
    for i in range(10):
        x, y = generate_integer(n)
        print(x, "+", y, "= ", end="")
        ans = int(input())
        if ans == x+y:
            pass
        else:
            print("EEE")
            j = j + 1
            ############################
            while True:
                print(x, "+", y, "= ", end="")
                ans = int(input())
                j = j + 1
                if j == 3:
                    print(x, "+", y, "= ", x+y)
                    break
                else:
                    if ans == x+y:
                        pass
                    else:
                        print("EEE")
            ############################
            score =score - 1
    print("Score:", score)


# if can't get the requested number, just loop forever
def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x in [1, 2, 3]:
                break
        except ValueError:
            pass
    return x

# return a tuple containing two numbers
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
