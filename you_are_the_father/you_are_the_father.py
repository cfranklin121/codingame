import sys
import math

def get_mother_child_chromPairs(person):
    lst = person.split()
    return lst[2:]

def get_father_info(person):
    lst = person.split()
    no_colan = lst[0].split(":")
    return no_colan[0], " ".join(lst[1:])

mother = input()
print(mother, type(mother))
mother_chrompairs = " ".join(get_mother_child_chromPairs(mother))
#print("Mother ChromPairs: ", mother_chrompairs)

child = input()
print(child, type(child))
child_chrompairs = get_mother_child_chromPairs(child)
#print("Child ChromPairs: ", child_chrompairs)
actual_father = "NONE"

num_of_possible_fathers = int(input())
x = 0
check = False
pair1 = False
pair2 = False
print(num_of_possible_fathers, type(num_of_possible_fathers))
for i in range(num_of_possible_fathers - 3):
    
    a_possible_father = input()
    #print(a_possible_father, type(a_possible_father))
    father_name, father_chrompairs = get_father_info(a_possible_father)
    print(father_name)
    print(father_chrompairs)

    check = True
    a = 0
    for pair in child_chrompairs:
        #false = 1st pair. true = 2nd pair
        #print(check)
        print(pair[0], pair[1])
        print("father: ", father_chrompairs[a], father_chrompairs[a+1])
        
        if pair[0] in mother_chrompairs[a] or pair[0] in mother_chrompairs[a+1]:
            x = 1
        if pair[1] in mother_chrompairs[a] or pair[1] in mother_chrompairs[a+1]:
            x = 0
        print("compare ", pair[x])
        if  father_chrompairs[a] in pair or father_chrompairs[a+1] in pair:
            print(f"Match pair{[x]} ", pair[x], father_name, father_chrompairs[a], father_chrompairs[a+1])
            
        else:
            check = False
        a += 3

    if check == True:
        actual_father = father_name
        print(f"Current father is {actual_father}")

if actual_father != "NONE":
    print(f"{actual_father}, you are the father!")