d = 50
while True:
    print("Amount Due:", d)
    x = int(input("Insert Coin: "))
    if x in [5, 10, 25]:
        d = d - x
        if d <= 0:
            print("Change Owed:", -d)
            break
        else:
            continue
    else:
        pass


