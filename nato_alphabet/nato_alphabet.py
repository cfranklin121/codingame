import sys
import math

a_word_spelled_out = input()

alpha_1 = ["Authority", "Bills", "Capture", "Destroy", "Englishmen", "Fractious", "Galloping", "High", "Invariably", "Juggling", "Knights", "Loose", "Managing", "Never", "Owners", "Play", "Queen", "Remarks", "Support", "The", "Unless", "Vindictive", "When", "Xpeditiously", "Your", "Zigzag"]
alpha_2 = ["Apples", "Butter", "Charlie", "Duff", "Edward", "Freddy", "George", "Harry", "Ink", "Johnnie", "King", "London", "Monkey", "Nuts", "Orange", "Pudding", "Queenie", "Robert", "Sugar", "Tommy", "Uncle", "Vinegar", "Willie", "Xerxes", "Yellow", "Zebra"]
alpha_3 = ["Amsterdam", "Baltimore", "Casablanca", "Denmark", "Edison", "Florida", "Gallipoli", "Havana", "Italia", "Jerusalem", "Kilogramme", "Liverpool", "Madagascar", "New-York", "Oslo", "Paris", "Quebec", "Roma", "Santiago", "Tripoli", "Uppsala", "Valencia", "Washington", "Xanthippe", "Yokohama", "Zurich"]
alpha_4 = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]

check_1 = True
check_2 = True
check_3 = True
check_4 = True

new_word = ""
words = a_word_spelled_out.split()
for word in words:
    if word not in alpha_1:
        check_1 = False
    if word not in alpha_2:
        check_2 = False
    if word not in alpha_3:
        check_3 = False
    if word not in alpha_4:
        check_4 = False

if check_1:
    for word in words:
        new_word += alpha_2[alpha_1.index(word)] + " "
if check_2:
    for word in words:
        new_word += alpha_3[alpha_2.index(word)] + " "
if check_3:
    for word in words:
        new_word += alpha_4[alpha_3.index(word)] + " "
if check_4:
    for word in words:
        new_word += alpha_1[alpha_4.index(word)] + " "

print(new_word.strip())