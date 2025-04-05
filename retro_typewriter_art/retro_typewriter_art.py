import sys
import math

t = input()

recipe = t.split()
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = {"sp" : " ", "bS" : "\\", "sQ" : "'"}

for a in range(len(recipe)):
    char = ""
    index = 0
    if recipe[a] == "nl":
        print()

    else:
        for i in range(len(recipe[a])):
            if recipe[a][i] in num:
                index = i

            if index == len(recipe[a]) - 1:
                index -= 1

            amount = int(recipe[a][:index + 1])            
            char = recipe[a][index + 1:]
            
        for x in range(amount):
            if char in special:
                print(special[char], end="")
            else:
                print(char, end="")
print()