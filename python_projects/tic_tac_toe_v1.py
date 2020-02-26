'''
Lab 26: Tic-Tac-Toe - Version 1

Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

Purpose/goal: Write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

'''
# the Player class has the following properties
class Player:
    # definte player token / name
    def __init__(self, token, name):
        self.token = token
        self.name = name
    # return token
    def __repr__(self):
        return self.token

# Board class defines the visualization / navigation of the game board
class Board:
    # game board y axis
    def __init__(self):
        self.board= [['_' for i in range(3)] for j in range(3)]
    # game board x axis
    def __repr__(self):
        display = ""
        for row in  self.board:
            display += "|".join(row)
            return display
    # designate player's token placement
    def place_token(self, token, x, y):
        if self.board[y][x] != "_":
            return 'That space is taken! Try again. '
            else:
                self.board[y][x] = token
    # determine winner when row of three 'spaces' filled
    def get_winner(self):
        for i in range(3):
            row = self.board[i]
            if row[0] == row[1] == row[2]:
                return row[0]

            column = [self.board[i][j] for j in range(3)]
            if col[0] ==  col[1] == col[2] and col[1] != "_":
                return col[0]
            
            if (self.board[0][0] == self.board[1][1] == self.board[0][0]) and self.board[0][0] != "_":
                return self.board[0][0]

            if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != "_":
                return self.board[1][1]
    # determine when board is full (draw)
    def is_full(self): 
        for row in self.board:
            for i in range(3):
                if row[i] == "_":
                    return False
            return True
    
    def is_game_over(self):
        if self.is_full() == True:
            return self.get_winner()
