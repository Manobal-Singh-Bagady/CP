# ---------------- MSB's Coding Template ---------------- #
"""
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
"""

# ---I/O from file---#
import sys
import math

try:
    sys.stdin = open("input.txt", "r", encoding="UTF-8")
    sys.stdout = open("output.txt", "w", encoding="UTF-8")
    sys.stderr = open("output.txt", "w", encoding="UTF-8")
except FileNotFoundError as __:
    pass


# ---------------------- Code Starts Here ----------------------#
def game_operation(X, Y, K):
    # for i in range(K*2):
    #     if i % 2 == 0:
    #         X, Y = min(X, Y), math.gcd(X, Y)
    #     else:
    #         X, Y = max(X, Y), math.lcm(X, Y)
    # return X + Y
    return math.lcm(min(X, Y), math.gcd(X, Y)) + math.gcd(X, Y)


for t in range(int(input())):
    X, Y, K = map(int, input().split())
    print(game_operation(X, Y, K))
