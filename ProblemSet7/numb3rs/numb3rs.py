import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        for i in ip.split("."):
            if int(i) < 0 or int(i) > 255:
                return False
    except ValueError:
        return False
    if re.search(r"^(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False




if __name__ == "__main__":
    main()
