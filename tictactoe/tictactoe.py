"""
Teeron Hajebi Tabrizi
February 7th, 2022

A program allowing two players to play tic tac toe against each other.
Base of a later program where the user will play against an AI.

"""

# I hope you have/had (based on when you review this) a very restful Ski Week!
import random

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to Tic Tac Toe. \nPlayer 1 is X and Player 2 is O. \nTake turns placing your pieces. The first player to get 3 in a row wins.")

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        for row in range(len(self.board)):
            row_string = str(row) + "\t"
            for col in range(len(self.board[0])):
                row_string += self.board[row][col] + "\t"
            print(row_string)

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if 0 <= row <= len(self.board) - 1 and 0 <= col <= len(self.board[0]) - 1:
            if self.board[row][col] == "-":
                return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        input_row = int(input("Enter a row: "))
        input_col = int(input("Enter a col: "))

        while not self.is_valid_move(input_row, input_col):
            print("Please enter a valid move.")
            input_row = int(input("Enter a row: "))
            input_col = int(input("Enter a col: "))

        self.place_player(player, input_row, input_col)

    def take_random_turn(self, player):
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)
        while not self.is_valid_move(rand_row, rand_col):
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
        print("Enter a row: " + str(rand_row))
        print("Enter a col: " + str(rand_col))
        self.place_player(player, rand_row, rand_col)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(str(player) + "'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player)

    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player)
        self.place_player(player, row, col)

    # Used you pseudo-code to write the minimax function
    # I was writing a different version of it, without using you
    # structure as much but I'm sick so I couldn't really debug it
    # and just decided to take the easy route. Sorry
    def minimax(self, player):
        if (self.check_win("O")):
            return 10, None, None
        elif (self.check_win("X")):
            return -10, None, None
        elif(self.check_tie()):
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
                        score = self.minimax("X")[0]
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
                        score = self.minimax("O")[0]
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

    def check_col_win(self, player):
        # TODO: Check col win
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    def check_tie(self):
        # TODO: Check tie
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == "-":
                    return False
        return True

    def play_game(self):
        # TODO: Play game
        game = True
        player = "X"
        self.print_instructions()
        self.print_board()
        while game:
            self.take_turn(player)
            if self.check_win(player):
                print(str(player) + " wins!")
                game = False
            elif self.check_tie():
                print("Tie game!")
                game = False
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            self.print_board()