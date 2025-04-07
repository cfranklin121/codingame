import sys
import math

def get_mother_child_chromPairs(person):
    lst = person.split()
    return lst[2:]

def get_father_info(person):
    lst = person.split()
    no_colon = lst[0].split(":")
    return no_colon[0], " ".join(lst[1:])

mother = input()
mother_chrompairs = get_mother_child_chromPairs(mother)

child = input()
child_chrompairs = get_mother_child_chromPairs(child)

actual_father = "NONE"
num_of_possible_fathers = int(input())
check = False

for i in range(num_of_possible_fathers):    
    a_possible_father = input()
    father_name, father_chrompairs = get_father_info(a_possible_father)
    
    check = True
    a = 0
    for pair in child_chrompairs:      
        if father_chrompairs[a] not in pair and father_chrompairs[a+1] not in pair:
            check = False
        a += 3

    if check == True:
        actual_father = father_name

if actual_father != "NONE":
    print(f"{actual_father}, you are the father!")