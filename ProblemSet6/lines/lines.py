import sys

ls = sys.argv
if len(ls) == 1:
    sys.exit("Too few command-line arguments")
elif len(ls) > 2:
    sys.exit("Too many command-line arguments")
elif ls[1].endswith(".py") == False:
    sys.exit("Not a Python file")
else:
    try:
        i = 0
        with open(ls[1]) as file:
            for line in file:
                if line.rstrip() == "" or line.rstrip()[0] == "#":
                    continue
                else:
                    i +=1
            print(i)

    except FileNotFoundError:
        sys.exit("File does not exist")

