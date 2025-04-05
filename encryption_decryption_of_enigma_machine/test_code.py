import sys
import math

#VS Code Test Version

def scramble(message, rotor):
    scrambled_message = ""
    for i in range(len(message)):
        index = (alpha.find(message[i]))
        scrambled_message += rotor[index]
    return scrambled_message

def descramble(message, rotor):
    scrambled_message = ""
    for i in range(len(message)):
        index = (rotor.find(message[i]))
        scrambled_message += alpha[index]
    return scrambled_message


operation = "DECODE"
pseudo_random_number = 9
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor_1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE" 
rotor_3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ" 
message = "PQSACVVTOISXFXCIAMQEM"

new_message_1 = ""
x = pseudo_random_number

if operation == "ENCODE":
    for i in range(len(message)):
        if x >= 26:
            x = 0

        index = (alpha.find(message[i]))
        
        if index + x >= 26: 
            index = index - 26
            
        new_message_1 = new_message_1 + alpha[index + x]
        x += 1

    new_message_2 = scramble(new_message_1, rotor_1)
    new_message_3 = scramble(new_message_2, rotor_2)
    final_message = scramble(new_message_3, rotor_3)
    

else:
    new_message_1 = descramble(message, rotor_3)
    new_message_2 = descramble(new_message_1, rotor_2)
    new_message_3 = descramble(new_message_2, rotor_1)
    final_message = ""

    for i in range(len(new_message_3)):
        if x >= 26:
            x = 0

        index = (alpha.find(new_message_3[i]))
        
        if index - x < 0: 
            index = index + 26

        final_message = final_message + alpha[index - x]
        x += 1

print(final_message)
