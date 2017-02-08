import nuclear_ttt
import grid_space
import sys
import os


class GameTime(object):
    def __init__(self, game_space):
        self.game = game_space
        self.game.init()
        self.game.update_map()
        self.turn = 0

    def turn():
        game.print_grid()
        game.print_game_stats()


y = GameTime(grid_space.GameSpace(25,25))


# GAME LOOP
exit = False
while(!exit):

    turn_done = False
    while(!turn_done):
        


y.game.print_grid()
y.game.print_game_stats()
