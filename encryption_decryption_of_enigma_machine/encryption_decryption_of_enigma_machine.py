import sys
import math

#Version 2.

def scramble(message, rotor, alpha):
    scrambled_message = ""
    for i in range(len(message)):
        index = (alpha.find(message[i]))
        scrambled_message += rotor[index]
    return scrambled_message

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

operation = input()
x = int(input()) #pseudo_random_number
rotor_1 = input()
rotor_2 = input()
rotor_3 = input()
message = input()

if operation == "ENCODE":
    new_message = ""
    for i in range(len(message)):
        if x >= 26:
            x = 0

        index = (alpha.find(message[i]))        
        if index + x >= 26: 
            index = index - 26
            
        new_message = new_message + alpha[index + x]
        x += 1

    final_message = scramble(scramble(scramble(new_message, rotor_1, alpha), rotor_2, alpha), rotor_3, alpha)
    
else:
    final_message = ""
    new_message = scramble(scramble(scramble(message, alpha, rotor_3), alpha, rotor_2), alpha, rotor_1)    
    for i in range(len(new_message)):
        if x >= 26:
            x = 0

        index = (alpha.find(new_message[i]))        
        if index - x < 0: 
            index = index + 26

        final_message = final_message + alpha[index - x]
        x += 1

print(final_message)