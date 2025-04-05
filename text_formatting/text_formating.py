import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

intext = input()

# 1) Lower case
intext = intext.lower()

#----------------------------------------------------

# 2) Remove extra punctuation
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == ',' and intext[y + 1] == ',':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1

  if intext[y] == '.' and intext[y + 1] == '.':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1
  if intext[y] == ',' and intext[y + 1] == '.':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1

  if intext[y] == '.' and intext[y + 1] == ',':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1
  y = y + 1


#----------------------------------------------------

# 3) Add spaces after punctuation
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == '.' or intext[y] == ',' and intext[y + 1] != ' ':
    intext = intext[:y+1] + ' ' + intext[y+1:]
    x = x + 1
  y = y + 1

#-----------------------------------------------------

# 4) Remove extra spaces
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == ' ' and intext[y + 1] == ' ':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1
  y = y + 1

#-----------------------------------------------------

# 5) Remove spaces before punctuation
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == ' ' and intext[y + 1] == ',':
    intext = intext[:y] + intext[y+1:]
    x = x + 1
    y = y - 1
  if intext[y] == ' ' and intext[y + 1] == '.':
    intext = intext[:y] + intext[y+1:]
    x = x + 1
    y = y - 1
  y = y + 1

#-----------------------------------------------------

# 6) Remove extra punctuation... again
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == ',' and intext[y + 1] == ',':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1

  if intext[y] == '.' and intext[y + 1] == '.':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1
  if intext[y] == ',' and intext[y + 1] == '.':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1

  if intext[y] == '.' and intext[y + 1] == ',':
    intext = intext[:y+1] + intext[y+2:]
    x = x + 1
    y = y - 1
  y = y + 1

#-----------------------------------------------------

# 7) Capitalize first word
textlower = intext[0]
intext = textlower.upper() + intext[1:]

#-----------------------------------------------------

# 8) Capitalize after period
x = 1
y = 0
for i in range(len(intext) - x):
  if intext[y] == '.' and intext[y + 1] == ' ':
    textlower = intext[y + 2]
    intext = intext[:y + 2] + textlower.upper() + intext[y + 3:]
    x = x + 1
    y = y - 1
  y = y + 1

print(intext)