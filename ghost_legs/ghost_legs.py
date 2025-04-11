import sys
import math

w, h = [int(i) for i in input().split()]
print(w)
print(h)
for i in range(h):
    line = input()
    #print(line, type(line))
    top_row = []
    for a in range(0, w, 3):
        if i == 0 or i == h:
            print(line[a], end="")
        else:
            print(line[a], end="")
    print("\n")


print("answer")