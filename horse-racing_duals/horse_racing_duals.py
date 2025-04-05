import sys
import math

strength = []
dif = []
n = int(input())
for i in range(n):
    pi = int(input())
    strength.append(pi)

strength = sorted(strength, reverse = True)

x = 0
while x < len(strength) - 1:
    dif.append(strength[x] - strength[x+1])
    x = x + 1

dif = sorted(dif)

print(dif[0])