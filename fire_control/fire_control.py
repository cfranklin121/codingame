import sys
import math


def cut(forest, h, w, trees_cut):
    forest[h][w] = "="
    trees_cut += 1
    return forest, trees_cut

forest = []
trees_cut = 0
total_trees = 0
fire = False
for i in range(6):
    text = input()
    forest.append(list(text))

for h in range(6):
    for w in range(6):
        if forest[h][w] == "#":
            total_trees += 1
        if forest[h][w] == "*":
            fire = True        
            #Cut up
            if h >= 1:
                if forest[h - 1][w] == "#":
                    forest, trees_cut = cut(forest, h - 1, w, trees_cut)
            if h >= 2:
                if forest[h - 2][w] == "#":
                    forest, trees_cut = cut(forest, h - 2, w, trees_cut)

            #Cut down
            if h <= 4:
                if forest[h + 1][w] == "#":
                    forest, trees_cut = cut(forest, h + 1, w, trees_cut)
            if h <= 3:
                if forest[h + 2][w] == "#":
                    forest, trees_cut = cut(forest, h + 2, w, trees_cut)

            #Cut left
            if w >= 1:
                if forest[h][w - 1] == "#":
                    forest, trees_cut = cut(forest, h, w - 1, trees_cut)
            if w >= 2:
                if forest[h][w - 2] == "#":
                    forest, trees_cut = cut(forest, h, w - 2, trees_cut)

            #Cut right
            if w <= 4:
                if forest[h][w + 1] == "#":
                    forest, trees_cut = cut(forest, h, w + 1, trees_cut)
            if w <= 3:
                if forest[h][w + 2] == "#":
                    forest, trees_cut = cut(forest, h, w + 2, trees_cut)

for h in range(6):
    for w in range(6):
        if forest[h][w] == "*":
            #up and left
            if h >= 1 and w >= 1:
                if forest[h - 1][w - 1] == "#":
                    forest, trees_cut = cut(forest, h - 1, w - 1, trees_cut)
            if h >= 2 and w >= 1:
                if forest[h - 2][w - 1] == "#":
                    forest, trees_cut = cut(forest, h - 2, w - 1, trees_cut)
            if h >= 1 and w >= 2:
                if forest[h - 1][w - 2] == "#":
                    forest, trees_cut = cut(forest, h - 1, w - 2, trees_cut)
            if h >= 2 and w >= 2:
                if forest[h - 2][w - 2] == "#":        
                    forest, trees_cut = cut(forest, h - 2, w - 2, trees_cut)

            #up and right
            if h >= 1 and w <= 4:
                if forest[h - 1][w + 1] == "#":
                    forest, trees_cut = cut(forest, h - 1, w + 1, trees_cut)
            if h >= 2 and w <= 4:
                if forest[h - 2][w + 1] == "#":
                    forest, trees_cut = cut(forest, h - 2, w + 1, trees_cut)
            if h >= 1 and w <= 3:
                if forest[h - 1][w + 2] == "#":
                    forest, trees_cut = cut(forest, h - 1, w + 2, trees_cut)
            if h >= 2 and w <= 3:
                if forest[h - 2][w + 2] == "#":        
                    forest, trees_cut = cut(forest, h - 2, w + 2, trees_cut)

            #down and left
            if h <= 4 and w >= 1:
                if forest[h + 1][w - 1] == "#":
                    forest, trees_cut = cut(forest, h + 1, w - 1, trees_cut)
            if h <= 3 and w >= 1:
                if forest[h + 2][w - 1] == "#":
                    forest, trees_cut = cut(forest, h + 2, w - 1, trees_cut)
            if h <= 4 and w >= 2:
                if forest[h + 1][w - 2] == "#":
                    forest, trees_cut = cut(forest, h + 1, w - 2, trees_cut)
            if h <= 3 and w >= 2:
                if forest[h + 2][w - 2] == "#":        
                    forest, trees_cut = cut(forest, h + 2, w - 2, trees_cut)

            #down and right
            if h <= 4 and w <= 4:
                if forest[h + 1][w + 1] == "#":
                    forest, trees_cut = cut(forest, h + 1, w + 1, trees_cut)
            if h <= 3 and w <= 4:
                if forest[h + 2][w + 1] == "#":
                    forest, trees_cut = cut(forest, h + 2, w + 1, trees_cut)
            if h <= 4 and w <= 3:
                if forest[h + 1][w + 2] == "#":
                    forest, trees_cut = cut(forest, h + 1, w + 2, trees_cut)
            if h <= 3 and w <= 3:
                if forest[h + 2][w + 2] == "#":        
                    forest, trees_cut = cut(forest, h + 2, w + 2, trees_cut)

if fire and trees_cut >= total_trees:
    print("JUST RUN")

elif fire:
    print(trees_cut)

else:
    print("RELAX")