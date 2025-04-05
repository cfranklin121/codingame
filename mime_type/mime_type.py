import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_type = {}

for i in range(n):
    ext, mt = input().split()
    mime_type[ext] = mt

for i in range(q):
    check = False
    fname = input()  # One file name per line.
    name = fname.split(".")

    for s in name[-1:]:
        f_ext = s.lower()
    
    for ext in mime_type:
        if ext.lower() == f_ext and "." in fname:
            print(mime_type[ext])
            check = True
            break
    
    if check == False:
        print("UNKNOWN")
