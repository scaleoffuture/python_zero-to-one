players = ['charlie', 'eliza', 'vin desiel', 'dragon', 'worm']
print(players[0:3])
print(players[1:3])

print(players[:5])

print(players[4:])

print(players[-3:])

print('Here are the first 3 players on my superteam:')
for player in players[2:]:
    print(player.title())