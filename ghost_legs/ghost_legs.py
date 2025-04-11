import sys
import math

w, h = [int(i) for i in input().split()]

line = []

for i in range(h):
    line.append(input())

for i in range(h):
      line[i] = " " + line[i] + " "


for x in range(1, w+1, 3):
    start = line[0][x]
    for i in range(1, h, 1):
        
        if line[i][x+1] == "-":
                x += 3
        
        elif line[i][x-1] == "-":
                x -= 3
        
    end = line[h-1][x]

    print(f"{start}{end}")
    