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


# ---------------------- Code Starts Here ----------------------#

for t in range(int(input())):
    n, m = map(int, input().split())
    x = str(input())
    s = str(input())

    if s in x:
        print(0)
        continue

    i = 1
    while True:
        if len(x) > 100000:
            print(-1)
            break
        x = x + x
        # print(x, i)
        if s in x:
            print(i)
            break
        i += 1
