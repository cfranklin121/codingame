import sys
import math

lst = input().split()

direction = lst[0]
num_arrows = int(lst[1])
height = int(lst[2])
stroke = int(lst[3])
space = int(lst[4])
indent = int(lst[5])

if direction == "right":
    dr = ">"
if direction == "left":
    dr = "<"

#RIGHT
if direction == "right":
    row = 0
    for c in range(height):
        if c < (height // 2): 
            row += 1
        else:
            row -= 1
        #Row
        for a in range(num_arrows):
            for i in range(stroke):
                print(dr, end="")
            if a < num_arrows - 1:
                for b in range(space):
                    print(" ", end="")
        
        print("")
        for d in range(indent*row):
            print(" ", end="")


#LEFT
if direction == "left":
    row = (height // 2) + 1
    for c in range(height):
        if c > (height // 2): 
            row += 1
        else:
            row -= 1

        
        for d in range(indent*row):
            print(" ", end="")

        #Row
        for a in range(num_arrows):
            for i in range(stroke):
                print(dr, end="")
            if a < num_arrows - 1:
                for b in range(space):
                    print(" ", end="")   
        print("")