# this project is for showcasing my phyton and im redoing an old project where java was used.
# The main goal is to create a simple sokoban game, first for the console 
# The second aim is to use pygame to create an interfase
# The thered aim is to create an AI that can solve the game

class Sokoban:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def find_player(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'P':
                    return row, col

        return -1, -1

    def move_player(self, direction):
        player_row, player_col = self.find_player()
        new_row, new_col = player_row, player_col

        if direction == 'up':
            new_row -= 1
        elif direction == 'down':
            new_row += 1
        elif direction == 'left':
            new_col -= 1
        elif direction == 'right':
            new_col += 1

        if self.board[new_row][new_col] != 'W':
            self.board[player_row][player_col] = ' '
            self.board[new_row][new_col] = 'P'

    def move_up(self):
        self.move_player('up')

    def move_down(self):
        self.move_player('down')

    def move_left(self):
        self.move_player('left')

    def move_right(self):
        self.move_player('right')

game_board = [
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'P', 'T', ' ', 'W'],
    ['W', ' ', ' ', ' ', 'W'],
    ['W', ' ', 'X', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W']
]

if __name__ == '__main__':

    game = Sokoban(game_board)
    game.print_board()
    direction = input("Enter direction (up, down, left, right): ")

    if direction == 'up':
        game.move_up()
    elif direction == 'down':
        game.move_down()
    elif direction == 'left':
        game.move_left()
    elif direction == 'right':
        game.move_right()

    game.print_board()