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


def findAnswer(n, m, arr):
    arr.sort(reverse=False)

    sum = 0

    for i in range(m):
        sum += (arr[i] + arr[n - i - 1]) * (arr[i] + arr[n - i - 1])

    return sum


N, M = map(int, input().split())
l = list(map(int, input().split()))[:N]

print(findAnswer(N, M, l))

# l.sort()
# ans = 0
# p = 1
# i = 0
# while i < N and p <= M:
#     temp = l[i]
#     i += 1
#     if i < N:
#         temp += l[i]
#         i += 1
#     ans += temp**2
#     p += 1
# print(ans)
