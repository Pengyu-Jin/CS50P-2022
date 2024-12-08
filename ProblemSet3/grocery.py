ls = {}
while True:
    try:
        item = input("").upper()
        if item not in ls:
            ls[item] = 1
        else:
            ls[item] = ls[item] + 1
    except EOFError:
        break

print()
ls_sorted = {j: ls[j] for j in sorted(ls)}
for i in ls_sorted:
    print (ls[i], i)

