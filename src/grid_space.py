import nuclear_ttt
from random import randint
from termcolor import colored
import colorama
from colorama import init
import sys
init()


class GameSpace(object):
    def __init__(self,row, col):
        self.row = row
        self.col = col
        self.players = []


        local_grid = [[]]
        i = 1
        while(i < self.col-1):
            local_grid.append([])
            j = 1
            local_grid[i].append(str("|"))
            while(j < self.row-1):
                local_grid[i].append(str("O"))
                j+=1
            local_grid[i].append(str("|"))
            i+=1
        self.grid = local_grid

    def add_player(self, player):
        player.position = [randint(4, self.row-4), randint(4, self.col-4)]
        self.players.append(player)

    def update_map(self):
        i = 1
        while(i < self.col-1):
            j = 1
            while(j < self.row-1):
                for player in self.players:
                    if int(player.position[0])==j and int(player.position[1])==i:
                        self.grid[i][j] = colored("X", player.color)
                j+=1
            i+=1






    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))

    def print_game_stats(self):
        i = 0
        line = []
        while(i < self.col*2):
            line.append("-")
            i+=1
        print(''.join(line))
        for player in self.players:
            px = str(player.position[0])
            py = str(player.position[1])
            coords = ','.join([px,py])

            print(colored(player.name, player.color))
            print(colored(("Postion: %s" % (coords)), player.color))
            print(colored((("Cash: $ %d") % (player.cash )), player.color))
            print()

    def init(self):
        done = False
        while not done:
            player = str(input("Add a player <name> <color>. Enter x when finished: "))
            if player == str("x"): done = True
            else:
                chars = player.split(' ')
                self.add_player(nuclear_ttt.Player(chars[0], chars[1]))




#
# game = GameSpace(25,25)
#
# u = nuclear_ttt.Player("Joe", "red")
#
# game.add_player(u)
#
# print(game.players[0].position)
# game.update_map()
#
#
# game.print_grid()
# game.print_game_stats()
# quit()
# exit()
# sys.exit()
