import sys
import math

l = int(input())
h = int(input())
t = input()
t = t.upper()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

letter = list(t)
letter_pos = []

for i in range(len(letter)):
    if letter[i] in alphabet:
        x = (alphabet.index(letter[i]) + 1)
        letter_pos.append(x)
    else:
        letter_pos.append(27)

for i in range(h):
    row = input()
    for y in range(len(letter)):
        end = (letter_pos[y]*l)
        start = (letter_pos[y]*l - l)
        print(row[start:end], end="")
        if y == len(letter) - 1:
            print("")