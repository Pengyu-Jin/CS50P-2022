import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r"src=\"(https?://(www.)?youtube.com/embed/.+?)\"", s)
    if match:
        src = match.group(1)
        tr = match.group(2)
        if tr is None:
            src_out = src.replace("youtube.com/embed", "youtu.be")
        else:
            src_out = src.replace("www.youtube.com/embed", "youtu.be")
        if src_out.startswith("http://"):
            src_out = src_out.replace("http://", "https://", 1)
        return src_out
    else:
        return None


if __name__ == "__main__":
    main()
