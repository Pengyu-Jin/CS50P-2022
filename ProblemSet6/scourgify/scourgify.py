import sys
import csv

ls = sys.argv

if len(ls) <= 2:
    sys.exit("Too few command-line arguments")
elif len(ls) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(ls[1]) as file_in:
            reader = csv.DictReader(file_in)
            with open(ls[2], "w") as file_out:
                writer = csv.DictWriter(file_out, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    lastname, firstname = row["name"].split(", ")
                    writer.writerow({"first": firstname, "last": lastname, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {ls[1]}")
