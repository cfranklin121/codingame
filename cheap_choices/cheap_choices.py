import sys
import math

c = int(input())
p = int(input())
items = {}
orders = {}
for i in range(c):
    items[i] = input()
    
for i in range(p):
    orders[i] = input()

#Orders
for i in range(p):
    min_price = None
    sold = False
    order = orders[i].split()
   
    #Loop and compare to each order to all items
    for x in range(c):
        item = items[x].split()
        
        if order[0] == item[0] and order[1] == item[1]: #Match Item
            sold = True
            if min_price == None:
                min_price = item[2]
                sold_item = x
            elif min_price > item[2]:
                min_price = item[2]
                sold_item = x
            
    if sold: #Remove sold item
        items[sold_item] = "SOLD"

    if min_price == None:
        print("NONE")
    else:
        print(min_price)