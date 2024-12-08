def main():
    while True:
        try:
            x = input("Fraction: ")
            n = convert(x)
            if n > 100:
                pass
            elif n < 0:
                pass
            else:
                print(gauge(n))
                break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    [X, Y] = fraction.split('/')
    o = 100*int(X)/int(Y)
    return int(f"{o:.0f}")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
