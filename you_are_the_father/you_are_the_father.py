import sys
import math

def get_mother_child_chromPairs(person):
    lst = person.split()
    return lst[2:]

def get_father_info(person):
    lst = person.split()
    return lst [0], " ".join(lst[1:])

mother = input()
print(mother, type(mother))
mother_chrompairs = get_mother_child_chromPairs(mother)
#print("Mother ChromPairs: ", mother_chrompairs)

child = input()
print(child, type(child))
child_chrompairs = get_mother_child_chromPairs(child)
#print("Child ChromPairs: ", child_chrompairs)

num_of_possible_fathers = int(input())

print(num_of_possible_fathers, type(num_of_possible_fathers))
for i in range(num_of_possible_fathers):
    a_possible_father = input()
    #print(a_possible_father, type(a_possible_father))
    father_name, father_chrompairs = get_father_info(a_possible_father)
    #print(father_name)
    #print(father_chrompairs)
    for pair in child_chrompairs:
        print(pair[0], pair[1])
        print("father: ", father_chrompairs)
        
        if pair[0] in father_chrompairs or pair[1] in father_chrompairs:
            print("pair ", pair, "father ", father_chrompairs)


print("what Maury Povich might say")