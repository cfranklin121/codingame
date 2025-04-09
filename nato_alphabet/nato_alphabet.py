import sys
import math

def convert(word, old_alpha, new_alpha):
    print("***IN FUNCTION***")
    print("Word: ", word)
    print("Old alphabet: ", old_alpha)
    print("New alphabet: ", new_alpha)
    if word in old_alpha:
        print(True)
    i = old_alpha.index(word)
    return new_alpha[i]

a_word_spelled_out = input()
alpha_1 = ["Authority", "Bills", "Capture", "Destroy", "Englishmen", "Fractious", "Galloping", "High", "Invariably", "Juggling", "Knights", "Loose", "Managing", "Never", "Owners", "Play", "Queen", "Remarks", "Support", "The", "Unless", "Vindictive", "When", "Xpeditiously", "Your", "Zigzag"]
alpha_2 = ["Apples", "Butter", "Charlie", "Duff", "Edward", "Freddy", "George", "Harry", "Ink", "Johnnie", "King", "London", "Monkey", "Nuts", "Orange", "Pudding", "Queenie", "Robert", "Sugar", "Tommy", "Uncle", "Vinegar", "Willie", "Xerxes", "Yellow", "Zebra"]
alpha_3 = ["Amsterdam", "Baltimore", "Casablanca", "Denmark", "Edison", "Florida", "Gallipoli", "Havana", "Italia", "Jerusalem", "Kilogramme", "Liverpool", "Madagascar", "New-York", "Oslo", "Paris", "Quebec", "Roma", "Santiago", "Tripoli", "Uppsala", "Valencia", "Washington", "Xanthippe", "Yokohama", "Zurich"]
alpha_4 = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]

print(
    f"Word spelled out: {a_word_spelled_out}",
      type(a_word_spelled_out),
        file=sys.stderr, flush=True
        )

new_word = ""
words = a_word_spelled_out.split()

for word in words:
    print("Word: ", word)
    if word in alpha_1:
        new_word += convert(word, alpha_1, alpha_2) + " "
    elif word in alpha_2:
        new_word += convert(word, alpha_2, alpha_3) + " "
    elif word in alpha_3:
        new_word += convert(word, alpha_3, alpha_4) + " "
    elif word in alpha_4:
        new_word += convert(word, alpha_4, alpha_1) + " "

final = new_word.strip()
print(final)
