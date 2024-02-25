# this project is for showcasing my phyton and im redoing an old project where java was used.
# The main goal is to create a simple sokoban game, first for the console 
# The second aim is to use pygame to create an interfase
# The thered aim is to create an AI that can solve the game

from Map import Map
from GameLogic import SokobanGame

game_board = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'P', ' ', ' ', 'W', ' ', ' ', 'X', 'W'],
    ['W', ' ', ' ', 'B', 'W', ' ', ' ', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
]

map_obj = Map(game_board)
game = SokobanGame(map_obj, 1, 1)

game.display()

while not game.is_completed:
    direction = input("Enter direction (W/A/S/D): ").upper()
    if direction == 'W':
        game.move_player(-1, 0)
    elif direction == 'A':
        game.move_player(0, -1)
    elif direction == 'S':
        game.move_player(1, 0)
    elif direction == 'D':
        game.move_player(0, 1)
    else:
        print("Invalid input!")





'''

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

    game.print_board()'''