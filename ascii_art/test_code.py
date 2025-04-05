import sys
import math

l = 4
h = 5
t = "ManhAtTan"
t = t.upper()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

letter = list(t)
letter_pos = []

rows = [" #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###",
        "# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #",
        "### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##",
        "# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #      ",
        "# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  # "
]

for i in range(len(letter)):
    if letter[i] in alphabet:
        x = (alphabet.index(letter[i]) + 1)
        letter_pos.append(x)
    else:
        letter_pos.append(27)

for i in range(h):
    row = rows[i]
    for y in range(len(letter)):
        end = (letter_pos[y]*l)
        start = (letter_pos[y]*l - l)
        print(row[start:end], end="")
        if y == len(letter) - 1:
            print("")