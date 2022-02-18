"""
Teeron Hajebi Tabrizi
February 18th, 2022

A program allowing two players to play tic tac toe against each other.
Base of a later program where the user will play against AIs of varying
strength.

"""

# I hope you have/had (based on when you review this) a very restful Ski Week!
# I changed the arguments for the take_turn method
import random


class TicTacToe:
    def __init__(self):
        # Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    # Prints the instructions of the game and asks the player if they want to play
    # against a friend or the AI.
    def print_instructions(self):
        # Print the instructions to the game
        print("Welcome to Tic Tac Toe. \nPlayer 1 is X and Player 2 is O. \nTake turns placing your pieces. The first player to get 3 in a row wins.")
        return input("Would you like to play against a friend or the computer? (Enter F or C): ")

    # Prints the board. Used when game is updates as well.
    def print_board(self):
        # Print the board
        print("\t0\t1\t2")
        for row in range(len(self.board)):
            row_string = str(row) + "\t"
            for col in range(len(self.board[0])):
                row_string += self.board[row][col] + "\t"
            print(row_string)

    # Checks if a move made by the user or AI is valid.
    def is_valid_move(self, row, col):
        # Check if the move is valid
        if (0 <= int(row) <= len(self.board) - 1 and 0 <= int(col) <= len(self.board[0]) - 1):
            if (self.board[int(row)][int(col)] == "-"):
                return True
        return False

    # Places the player in the given row and column.
    def place_player(self, player, row, col):
        # Place the player on the board
        self.board[row][col] = player

    # Called when the user(s) wants to play the game.
    def take_manual_turn(self, player):
        # Ask the user for a row, col until a valid response
        # is given them place the player's icon in the right spot

        input_row = input("Enter a row: ")
        input_col = input("Enter a col: ")

        while ((input_row == '' or input_col == '') or (self.is_valid_move(input_row, input_col) is False)):
            print("Please enter a valid move.")
            input_row = input("Enter a row: ")
            input_col = input("Enter a col: ")

        self.place_player(player, int(input_row), int(input_col))

    # Weaker version of AI that does not apply logic to solve the problem.
    def take_random_turn(self, player):
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)

        while not self.is_valid_move(rand_row, rand_col):
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)

        self.place_player(player, rand_row, rand_col)

    # Calls the other methods to allow the game to be played.
    def take_turn(self, player, game_mode, depth):

        print(str(player) + "'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        elif (game_mode == "C"):
            self.take_minimax_turn(player, depth)
        elif (game_mode == "F"):
            self.take_manual_turn("O")

    # Wrapper function of the minimax AI.
    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax(player, depth)
        #if (self.is_valid_move(row, col)):
        self.place_player(player, row, col)

    # Implementation of the minimax AI.
    def minimax(self, player, depth):
        # Used you pseudo-code to write the minimax function
        # I was writing a different version of it, without using you
        # structure as much but I'm sick so I couldn't really debug it
        # and just decided to take the easy route. Sorry
        if (self.check_win("O")):
            return 10, None, None
        elif (self.check_win("X")):
            return -10, None, None
        elif(self.check_tie() or depth == 0):
            return 0, None, None

        opt_row, opt_col = -1, -1
        if player == "O":
            best = -10
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    # My (fruitless) attempt at writing all the innards of these
                    # nested for loops in one line.
                    # [self.place_player(player, row, col); score = self.minimax("X")[0]; self.place_player("-", row, col) if self.board[row][col] == "-" else ( best, opt_row, opt_col = score, row, col if best < score )]
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score = self.minimax("X", depth - 1)[0]
                        self.place_player("-", row, col)
                        if best < score:
                            best, opt_row, opt_col = score, row, col
            return best, opt_row, opt_col

        if player == "X":
            worst = 10
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score = self.minimax("O", depth - 1)[0]
                        self.place_player("-", row, col)
                        if worst > score:
                            worst, opt_row, opt_col = score, row, col
            return worst, opt_row, opt_col

        '''
        # alternative method of solving
        # I'm too sick to finish this version right now and debug
        # I'll come back to this some point soon because I think
        # It may be a more efficient method of solving this problem
        # If you have any idea what the error could be please let me
        # know lol
        best, row, col = 1000, None, None
        worst, row, col = -1000, None, None
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.is_valid_move(i, j):
                    self.place_player(player, i, j)
                    if (player == "O"):
                        score, r, c = self.minimax("X")
                    elif (player == "X"):
                        score, r, c = self.minimax("O")
                    if (score > best):
                        best, row, col = score, i, j
                    elif (score > worst):
                        worst, row, col = score, i, j
                    self.place_player("-", i, j)
        return score, row, col
        '''

    # Checks to see if there are three in a row in a column.
    def check_col_win(self, player):
        # TODO: Check col win
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        return False

    # Checks to see if there are three in a row in a row.
    def check_row_win(self, player):
        # TODO: Check row win
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        return False

    # Checks to see if there are three in a row in a diagonal.
    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    # Checks to see if a player has won
    def check_win(self, player):
        # Check win
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    # Checks to see if there has been a draw.
    def check_tie(self):
        # TODO: Check tie
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == "-":
                    return False
        return True

    # Game is run through here. All other methods are called.
    def play_game(self):
        # TODO: Play game
        game = True
        player = "X"
        mode = self.print_instructions()

        # The line below is stupid because at any depth below 6
        # the AI essentially plays like the random bot. However, I feel like
        # I could find a way to add levels of difficulty through this.
        # depth = random.randint(3, 9)
        if (mode == 'C'):
            # The upper limit of 8 in unnecessary but it seems cooler for it
            # to be able to go up to level 5. At any point above 6 it becomes
            # unbeatable I think.
            depth = random.randint(4, 8)
            print("Level of AI: " + str(depth - 3))

        self.print_board()
        while game:
            self.take_turn(player, mode, depth)
            if self.check_win(player):
                print(str(player) + " wins")
                game = False
            elif self.check_tie():
                print("Tie game")
                game = False
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            self.print_board()