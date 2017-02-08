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
        self.newsreel = []


        local_grid = [[]]
        i = 0
        xc = 0
        while(i < self.col):
            local_grid.append([])
            j = 0
            if xc > 9: xc = 0
            local_grid[i].append(" ")
            local_grid[i].append(str(xc))
            local_grid[i].append(str("|"))
            while(j < self.row):
                local_grid[i].append(str("O"))
                j+=1
            local_grid[i].append(str("|"))
            local_grid[i].append(str(xc))
            xc+=1
            i+=1
        local_grid.remove(local_grid[i])
        self.grid = local_grid

    def add_player(self, player):
        player.position = [randint(4, self.row-4), randint(4, self.col-4)]
        self.players.append(player)

    def update_map(self):
        i = 0
        while(i < self.col):
            j = 0
            while(j < self.row):
                for player in self.players:
                    if int(player.position[0])==j and int(player.position[1])==i:
                        self.grid[i][j+3] = colored("X", player.color)
                j+=1
            i+=1



    def print_news_reel(self):
        print("-------------------------------------------------------")
        print("NEWS & BROADCASTS:")
        for line in self.newsreel:
            print(line)
        print("-------------------------------------------------------")
        print()

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def print_game_stats(self):
        i = 0
        xc = 0
        line = []
        line.append("     ")
        x = []
        x.append("     ")
        while(i < self.col):
            line.append("--")
            if xc > 9: xc = 0
            x.append(str(xc))
            i+=1
            xc+=1
        print(''.join(line))
        print(' '.join(x))
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
