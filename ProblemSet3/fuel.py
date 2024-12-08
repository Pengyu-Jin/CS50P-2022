while True:
    try:
        x = input("Fraction: ")
        [X, Y] = x.split('/')
        o = int(X)/int(Y)
        if o > 1:
            pass
        elif o >= 0.99:
            print("F")
            break
        elif o < 0:
            pass
        elif o <= 0.01:
            print("E")
            break
        else:
            print(f"{100*o:.0f}%")
            break
    except (ValueError, ZeroDivisionError):
        pass

