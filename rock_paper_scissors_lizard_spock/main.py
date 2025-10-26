

n = int(input())
player = []
player_stats = {}
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    player.append((numplayer, signplayer))
    player_stats[player[i]] = []


cont = True
while cont:
    winner = []
    for i in range(0, len(player)-1, 2):
        #Scissors cuts Paper
        if (player[i][1] == "C" and player[i+1][1] == "P") or (player[i+1][1] == "C" and player[i][1] == "P"):
            if player[i][1] == "C":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Paper Covers Rock
        if (player[i][1] == "P" and player[i+1][1] == "R") or (player[i+1][1] == "P" and player[i][1] == "R"):
            if player[i][1] == "P":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Rock crushes Lizard
        if (player[i][1] == "R" and player[i+1][1] == "L") or (player[i+1][1] == "R" and player[i][1] == "L"):
            if player[i][1] == "R":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Lizard Spock
        if (player[i][1] == "L" and player[i+1][1] == "S") or (player[i+1][1] == "L" and player[i][1] == "S"):
            if player[i][1] == "L":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Spock Scissors
        if (player[i][1] == "S" and player[i+1][1] == "C") or (player[i+1][1] == "S" and player[i][1] == "C"):
            if player[i][1] == "S":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Scissors Lizard
        if (player[i][1] == "C" and player[i+1][1] == "L") or (player[i+1][1] == "C" and player[i][1] == "L"):
            if player[i][1] == "C":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Lizard Paper
        if (player[i][1] == "L" and player[i+1][1] == "P") or (player[i+1][1] == "L" and player[i][1] == "P"):
            if player[i][1] == "L":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Paper Spock
        if (player[i][1] == "P" and player[i+1][1] == "S") or (player[i+1][1] == "P" and player[i][1] == "S"):
            if player[i][1] == "P":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Spock Rock
        if (player[i][1] == "S" and player[i+1][1] == "R") or (player[i+1][1] == "S" and player[i][1] == "R"):
            if player[i][1] == "S":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])
        
        #Rock Scissors
        if (player[i][1] == "R" and player[i+1][1] == "C") or (player[i+1][1] == "R" and player[i][1] == "C"):
            if player[i][1] == "R":
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

        #Tie
        if player[i][1] == player[i+1][1]:
            if player[i][0] < player[i+1][0]:
                winner.append(player[i])
                player_stats[player[i]].append(player[i+1][0])
            else:
                winner.append(player[i+1])
                player_stats[player[i+1]].append(player[i][0])

    player = winner
    if len(winner) <= 1:
        cont = False

print(player[0][0])
for i in range(len(player_stats[player[0]])):
    print(player_stats[player[0]][i], end="")
    if i < (len(player_stats[player[0]]) - 1):
        print(end=" ")
