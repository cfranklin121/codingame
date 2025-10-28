def ghost_legs(input):
    w, h = [int(i) for i in input[0].split()]
    line = []
    input.pop(0)
    result = []

    for i in range(h):
        line.append(input[i])
        line[i] = " " + line[i] + " "   

    j = 0
    for x in range(1, w+1, 3):
        print(line[0][x], end="")
        result.append(line[0][x])
        for i in range(1, h, 1):
            if line[i][x+1] == "-":                
                    x += 3
            elif line[i][x-1] == "-":                
                    x -= 3
        print(line[h-1][x])
        result[j] += (line[h-1][x])
        j+=1
    return result