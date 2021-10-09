"""
Game Preferences
Make a list that includes 3 or 4 games that you like to play.
Print a statement that tells the user what games you like.
Ask the user to tell you a game they like, and store the game
Add the user's game to your list.
Print a new statement that lists all of the games that we
like to play (we means you and your user).
"""

games = ['FIFA', 'NBA2k', 'CoD', 'Rainbow 6 Siege']
print("I like " + ', '.join(games[:-1]) + ", and " + games[-1])

userGames = input("What's a game that you like? ")

games.append(userGames)
print("We like " + ', '.join(games[:-1]) + ", and " + games[-1])