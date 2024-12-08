def main():
    x = input("")
    output = convert(x)
    print(output)

def convert(str):
    output = str.replace(":)", "🙂").replace(":(", "🙁")
    return output

main()
