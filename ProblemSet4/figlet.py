from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

# get a list of fonts
fontslist = figlet.getFonts()
n = len(fontslist)


# get the command line arguments
if len(sys.argv) > 3 or len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    seed = random.randint(0, n-1)
    figlet.setFont(font = fontslist[seed])
    x = input("Input: ")
    print("Output:\n" + figlet.renderText(x))
else:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fontslist:
        figlet.setFont(font = sys.argv[2])
        x = input("Input: ")
        print("Output:\n" + figlet.renderText(x))
    else:
        sys.exit("Invalid usage")
