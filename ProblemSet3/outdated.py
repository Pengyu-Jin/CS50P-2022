month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    try:
        x = input("Date: ")
        [m, d, y] = x.split("/")
        [M, D, Y] = [int(m), int(d), int(y)]
        if 0 < M <=12 and 0 < D <=31:
            print(f"{Y:04}-{M:02}-{D:02}")
            break
    except (NameError, ValueError):
        pass
    try:
        [s, y] = x.split(",")
        [m, d] = s.split(" ")
        if 0 < int(d) <=31:
            if m in month:
                m = month.index(m) +1
                print(f"{int(y):04}-{int(m):02}-{int(d):02}")
                break
    except (NameError, ValueError):
        pass
