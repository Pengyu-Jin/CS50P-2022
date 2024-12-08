from tabulate import tabulate
import sys

ls = sys.argv
if len(ls) == 1:
    sys.exit("Too few command-line arguments")
elif len(ls) > 2:
    sys.exit("Too many command-line arguments")
elif ls[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        lines = []
        with open(ls[1]) as file:
            for line in file:
                lines.append(line.rstrip().split(","))
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

