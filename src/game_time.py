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
        print("[1] Broadcast")
        print("[2] Private Message")
        print("[3] Intelligence Center")
        print("[4] Defense Center")
        print("[5] Payment")
        print("[6] Store")
        print("[7] END TURN")
        print("[q] Exit Game")
        print("")
        action = input("$ ")

        # MOVEMENT
        if action in ["w", "a", "s", "d"] and move_tokens < 5:
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

        # BROADCAST

        # PRIVATE Message

        # Intelligence CENTER
        if action is "3":
            print("Welcome to the Intelligence Center: ")
            print("-------------------------------")
            print("     Missle Count:", 0)
            print("     Our Controlled Space:", len(turn_player.explored))
            print("     Revenue per turn:  $", len(turn_player.explored)*50)
            print("     Inventory:")
            print("-------------------------------")
            report_done = input("$ Press enter to finish.")


        # DEFENSE CENTER
        if action is "4":
            print("Welcome to the Defense Center: ")
            print("-------------------------------")
            print("     Missle Count: ")
            print("     Controlled Space: ")
            print("-------------------------------")
            print("Options: ")
            print("[1] Message opponent")
            print("[2] Initiate nuclear missle launch")
            print("[3]")
            report_done = input("$ Press enter to finish.")

        # PAYMENT

        # STORE
        if action is "6":
            print("Welcome to the Store!:")
            print("1 [$10,000] Movement Speed - Move one more space per turn")
            print("2 [$25,000] Tax System - Get $10 more per tile you own")
            print("3 [$50,000] Iron Dome - Reduce your chance of getting nuked by 15 percent")
            print("4 [$75,000] Coup - Opponents tile can occasionally switch to your side")
            print("5 [$100,000] Ballistic Missle - Add a missle to your inventory")
            print("6 [$500,000] Rigged - hack an opponent and use their missles")
            print("7 [$1,000,000] Endgame - Unlimited Missles per turn")
            print ()
            report_done = input("$ Press enter to exit Store.")


        if action is "7":
            turn_done = True
            print("Turn over!")


        if action is "q":
            turn_done = True
            exit = True

    # POST turn



    y.turn+=1
    if y.turn+1 > len(y.game.players):
        y.turn = 0
        y.round+=1
