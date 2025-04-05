import sys
import math

c = 3
p = 2
items = {}
orders = {}

item_input = [
    "JEANS LARGE 30",
    "SHIRT SMALL 15",
    "JACKET LARGE 20"
]

order_input = [
    "JEANS LARGE",
    "JACKET LARGE"
]

for i in range(c):
    item = item_input[i]
    items[i] = item
    #print(item)
for i in range(p):
    order = order_input[i]
    orders[i] = order

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