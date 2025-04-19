import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())

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
    else:
        for x in range(w+2):
            if x == 0 or x == w+1:
                box[i].append("|")
            else:
                box[i].append(" ")

for i in range(n):
    placed = False
    inputs = input().split()
    s = inputs[0]
    p = int(inputs[1])
    x = p + 1
    y = 0
    while not placed:
        if s.isupper():
            if box[y][x] == " ":
                pass
            elif x-1 != 0 and box[y][x-1] == " ":
                x = x-1
            elif x+1 != w+1 and box[y][x+1] == " ":
                x = x+1
            else:
                y -= 1
                box[y][x] = s
                placed = True
            
            if y == h - 1:
                box[y][x] = s
                placed = True
            y += 1

        elif s.islower():
            if box[y][x] == " ":
                pass
            elif x+1 != w+1 and box[y][x+1] == " ":
                x = x+1
            elif x-1 != 0 and box[y][x-1] == " ":
                x = x-1
            else:
                y -= 1
                box[y][x] = s
                placed = True
            
            if y == h - 1:
                box[y][x] = s
                placed = True
            y += 1

#Print box    
for i in range(h+1):
    for x in range(w+2):
        print(box[i][x], end="")
    print()