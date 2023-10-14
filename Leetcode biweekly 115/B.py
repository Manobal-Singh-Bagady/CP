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
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words, groups):
        res = []
        res.append(words[0])
        i = 0
        j = 1
        while i < j < n:
            if groups[i] != groups[j]:
                res.append(words[j])
                i = j
                j += 1
            else:
                j += 1
        return res
