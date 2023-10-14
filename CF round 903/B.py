# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""





# ---I/O from file---#


import sys



try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ----------------------   Code Starts Here   ----------------------#
for t in range(int(input())):
    l = list(map(int, input().split()))
    if l[0] == l[1] == l[2]:
        print("YES")
        continue
    for i in range(3):
        max_index = l.index(max(l))
        maxEle = l[max_index]
        minEle = min(l)
        l.append(minEle)
        l[max_index] = maxEle - minEle
        # print(l)
        if all(i == l[0] for i in l):
            print("YES")
            break
    else:
        print("NO")
