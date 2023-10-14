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
    def lastVisitedIntegers(self, words):
        nums = []
        result = []
        k = 0
        for word in words:
            if word == "prev":
                k += 1
                if k > len(nums):
                    result.append(-1)
                else:
                    result.append(nums[-k])
            else:
                nums.append(int(word))
                k = 0
        return result


ob = Solution()
arr = ["prev","prev","prev","1"]
print(ob.lastVisitedIntegers(arr))
