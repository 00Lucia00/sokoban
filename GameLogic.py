from Map import Map

class SokobanGame:
    def __init__(self, map_obj, player_row, player_col):
        self.map_obj = map_obj
        self.player_row = player_row
        self.player_col = player_col
        self.is_completed = False

    def display(self):
        self.map_obj.display()

    def move_player(self, d_row, d_col):
        new_row = self.player_row + d_row
        new_col = self.player_col + d_col

        if not self.map_obj.is_wall(new_row, new_col):
            if self.map_obj.is_box(new_row, new_col):
                # Check if the box can be pushed
                new_box_row = new_row + d_row
                new_box_col = new_col + d_col
                if not self.map_obj.is_wall(new_box_row, new_box_col) \
                        and not self.map_obj.is_box(new_box_row, new_box_col):
                    # Move the box
                    self.map_obj.layout[new_row][new_col] = ' '
                    self.map_obj.layout[new_box_row][new_box_col] = 'B'
                else:
                    return False
            self.map_obj.layout[self.player_row][self.player_col] = ' '
            self.player_row = new_row
            self.player_col = new_col
            self.map_obj.layout[self.player_row][self.player_col] = 'P'

        self.display()
        self.check_completion()
        return True

    def check_completion(self):
        if self.map_obj.is_completed():
            self.is_completed = True

'''class Sokoban:
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
        self.move_player('right')'''