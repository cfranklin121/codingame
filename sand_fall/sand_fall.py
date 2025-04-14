import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
print(f"w:{w} h:{h}")
print(f"n:{n}")
for i in range(n):
    inputs = input().split()
    s = inputs[0]
    p = int(inputs[1])
    print(f"s:{s} p:{p}")

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
box[h-1][p] = "x"
#box[h-1][p+1] = "x"
s = "A"
x = p
y = h


if s.isupper():
    if box[y-1][x] == " ":
        box[y-1][x] = s
    elif x-1 != 0 and box[y-1][x-1] == " ":
        box[y-1][x-1] = s
    elif x+1 != w+1 and box[y-1][x+1] == " ":
        box[y-1][x+1] = s

elif s.islower():
    if box[y-1][x] == " ":
        box[y-1][x] = s
    elif x+1 != w+1 and box[y-1][x+1] == " ":
        box[y-1][x+1] = s
    elif x-1 != 0 and box[y-1][x-1] == " ":
        box[y-1][x-1] = s

#Print box    
for i in range(h+1):
    for x in range(w+2):
        print(box[i][x], end="")
    print()