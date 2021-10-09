games = ['FIFA', 'NBA2k', 'CoD', 'Rainbow 6 Siege']
print("I like the games " + ', '.join(games[:-1]) + ", and " + games[-1])

userGames = " "
while True:
    userGames = input("What's a game that you like? (respond with \"quit\" to exit) ")
    games.append(userGames)
    if userGames == 'quit':
        break

print("We like the games " + ', '.join(games[:-1]) + ", and " + games[-1])
