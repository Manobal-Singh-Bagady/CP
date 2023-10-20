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
    N, K = map(int, input().split())
    l = list(map(int, input().split()))[:N]
    x = sum(l)
    if x < N:
        print("NO")
        continue
    res = [0] * (N)
    j = 0
    # for i in range(x):
    #     res[j] += 1
    #     j += 1
    #     if j == N:
    #         j = 0
    while x > N:
        x -= N
    res = [sum(l) - x] * N
    for i in range(x):
        res[i] += 1
    # print(res)
    if (max(res) - min(res)) <= K:
        print("YES")
    else:
        print("NO")
