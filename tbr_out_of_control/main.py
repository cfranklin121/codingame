import sys
import math

new_books = []
b = int(input())
for i in range(b):
    title = input()
    tup = (title, None)
    new_books.append(tup)
n = int(input())
bookshelf = []
for i in range(n):
    name = input()
    if name[-1].isdigit():
        tup = (name[:-2], int(name[-1]))
        bookshelf.append(tup)
    else:
        tup = (name[:-5], None)
        bookshelf.append(tup)

highest = float('-inf')
lowest = float('inf')

for book in bookshelf:
    if book[1] and book[1] < lowest:
        lowest = book[1]
    if book [1] and book[1] > highest:
        highest = book[1]

 
for new in new_books: #Remove duplcate titles
    for book in bookshelf:
        if new[0] == book[0]:
            bookshelf.remove(book)

for i in range(n): 
    if len(new_books) + len(bookshelf) <= n:
        break
    else:
        for book in bookshelf: #Remove bottom ranked
            if book[1] and book[1] <= lowest and lowest < highest:
                bookshelf.remove(book)
        for book in bookshelf: #Remove bottom ranked
            if book[1] and book[1] <= lowest and lowest < highest:
                bookshelf.remove(book)
        
        lowest = 11
        for book in bookshelf:
            if book[1] and book[1] < lowest:
                lowest = book[1]

if len(new_books) + len(bookshelf) > n:
    print("Your TBR is out of control Clara!")
else:
    for new in new_books:
        bookshelf.append(new)
    bookshelf = sorted(bookshelf)

    for book in bookshelf:
        print(book[0])
