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


def convert_words_to_digits(inp):
    # Mapping words to corresponding digits
    word_to_digit_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    word_list = inp.split()

    phone_number = ""
    index = 0
    while index < len(word_list):
        if word_list[index] == "double":
            digit = word_to_digit_map[word_list[index + 1]]
            phone_number += digit * 2
            index += 2
        elif word_list[index] == "triple":
            digit = word_to_digit_map[word_list[index + 1]]
            phone_number += digit * 3
            index += 2
        else:
            phone_number += word_to_digit_map[word_list[index]]
            index += 1

    return phone_number


if __name__ == "__main__":
    print(convert_words_to_digits(str(input())))
