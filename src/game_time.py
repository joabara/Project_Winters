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
        self.round = 0


    def start_turn():
        turn_player = self.game.players[self.turn]


os.system("cls")
y = GameTime(grid_space.GameSpace(30,30))


#GAME LOOP
exit = False

while not exit:

    turn_done = False
    turn_player = y.game.players[y.turn]
    move_tokens = 0
    turn_player.cash += len(turn_player.explored)*50

    while(turn_done is not True):
        os.system("cls")
        y.game.update_map()
        print("Round:", y.round, "Turn:", y.turn)
        y.game.print_grid()
        y.game.print_game_stats()

        print("It's", turn_player.name, "'s turn")

        print("[w,a,s,d] Move")
        print("[2] Broadcast")
        print("[3] Private Message")
        print("[4] Football")
        print("[5] Payment")
        print("[6] Store")
        print("[7] END TURN")
        print("[q] Exit Game")
        print("")
        action = input("$ ")

        # MOVEMENT
        if(action in ["w", "a", "s", "d"] and move_tokens < 3):
            if action is "w" :
                turn_player.position[1] = turn_player.position[1]-1
            if action is "a" :
                turn_player.position[0] = turn_player.position[0]-1
            if action is "s" :
                turn_player.position[1] = turn_player.position[1]+1
            if action is "d" :
                turn_player.position[0] = turn_player.position[0]+1

            for player in y.game.players:
                if player.name is not turn_player.name:
                    if [turn_player.position[0], turn_player.position[1]] in player.explored:
                        player.explored.remove(turn_player.position)
            turn_player.explored.append([turn_player.position[0], turn_player.position[1]])
            move_tokens+=1


        if action is "7":
            turn_done = True
            print("Turn over!")




        ### OTHER CONDITIONS
        # if move_tokens is 3:
        #     turn_done = True

        if action is "q":
            turn_done = True
            exit = True

    # POST turn



    y.turn+=1
    if y.turn+1 > len(y.game.players):
        y.turn = 0
        y.round+=1
