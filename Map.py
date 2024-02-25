# a class for creating the game map

class Map:
    def __init__(self, layout):
        self.layout = layout

    def display(self):
        for row in self.layout:
            print("".join(row))

    def is_wall(self, row, col):
        return self.layout[row][col] == 'W'

    def is_box(self, row, col):
        return self.layout[row][col] == 'B'

    def is_target(self, row, col):
        return self.layout[row][col] == 'X'

    def is_completed(self):
        for row in self.layout:
            if 'B' in row:
                return False
        return True



