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


def find_possible_strings(N, T_prime, S_list):
    possible_indices = []
    for i in range(N):
        S = S_list[i]
        if len(S) == len(T_prime):
            diff = sum(i != j for (i, j) in zip(S, T_prime))
            if diff in (1, 0):
                possible_indices.append(i + 1)
        elif len(S) == len(T_prime) - 1:
            for j in range(len(T_prime)):
                if T_prime[:j] + T_prime[j + 1 :] == S:
                    possible_indices.append(i + 1)
                    break
        elif len(S) == len(T_prime) + 1:
            for j in range(len(S)):
                if S[:j] + S[j + 1 :] == T_prime:
                    possible_indices.append(i + 1)
                    break
    return len(possible_indices), possible_indices


n, T = input().split()
n = int(n)
T = str(T)
sList = []
for t in range(n):
    sList.append(str(input()))
a, l = find_possible_strings(n, T, sList)
print(a)
print(*l)
