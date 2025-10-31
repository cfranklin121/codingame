def unary(input):
    #Input
    message = input
    binary_message = "" #Create enpty string for the binary message

    for char in list(message):
        binary_message = binary_message + (format(ord(char), "07b"))
    binary_message = binary_message + "x" #Add extra character to avoid an out of range index error

    index = [0] #List of every index that stars a different groupd of numbers

    for i in range(len(binary_message) - 1):
        if binary_message[i] != binary_message[i + 1]:
            index.append(i + 1)

    character_count = [] #Number of 0's or 1's in each group

    for i in range(len(index) - 1):
        character_count.append(index[i + 1] - index[i])

    #Output
    result = ""
    for i in range(len(index) - 1):
        if binary_message[index[i]] == "1":
            #print("0", end=" ")
            result += "0" + " "
        if binary_message[index[i]] == "0":
            #print("00", end=" ")
            result += "00" + " "
        for x in range(character_count[i]):
            #print("0", end= "")
            result += "0"
        if i < (len(index) - 2):
            #print(end=" ")
            result += " "
    return result
