import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())

'''
for i in range(n):
    inputs = input().split()
    s = inputs[0]
    p = int(inputs[1])
    print(f"s:{s} p:{p}")
'''

#Build the box
box = []
for i in range(h+1):
    box.append([])
    if i == h:
        for x in range(w+2):
            if x == 0 or x == w+1:
                box[i].append("+")
            else:
                box[i].append("-")
            print(box[i][x], end="")
        print()
    else:
        for x in range(w+2):
            if x == 0 or x == w+1:
                box[i].append("|")
            else:
                box[i].append(" ")
            print(box[i][x], end="")
        print()

p = 2
#box[h-1][p] = "x"
#box[h-1][p+1] = "x"

y = h - 1
full = False


a = 0
for i in range(n):
    placed = False
    inputs = input().split()
    s = inputs[0]
    p = int(inputs[1])
    x = p + 1
    while not placed:
        if s.isupper():
            if box[y][x] == " ":
                box[y][x] = s
                placed = True
            elif x-1 != 0 and box[y][x-1] == " ":
                box[y][x-1] = s
                placed = True
            elif x+1 != w+1 and box[y][x+1] == " ":
                box[y][x+1] = s
                placed = True
            else:
                y -= 1

        elif s.islower():
            if box[y][x] == " ":
                box[y][x] = s
                placed = True
            elif x+1 != w+1 and box[y][x+1] == " ":
                box[y][x+1] = s
                placed = True
            elif x-1 != 0 and box[y][x-1] == " ":
                box[y][x-1] = s
                placed = True
            else:
                y -= 1


    for i in range(h+1):
        for x in range(w+2):
            print(box[i][x], end="")
        print()
    a += 2
#Print box    
for i in range(h+1):
    for x in range(w+2):
        print(box[i][x], end="")
    print()