import random

from dreidel import Dreidel
from player import Player
from pot import Pot
from user_input import get_integer

class Game:

    __INITIAL_NUM_COINS = 8


    def __init__(self):
        self.__pot = Pot()
        self.__rounds = random.randint(3,10)
        self.__players = self.__initialize_players()
        self.__initialize_pot()

    def __str__(self):
        return f"pot: {str(self.__pot)}"

    # ------------------------------------------------------------------ setup
    def __initialize_players(self):
        num_players = get_integer("how many players",5,2)
        players = []
        for pix in range(num_players):
            name = input(f"what is the name of player {pix+1}? ")
            color = input(f"what color is {name}'s dreidel? ")
            player = Player(name,Dreidel(color))
            player.add_coins(self.__INITIAL_NUM_COINS)
            players.append(player)
        return players

    def __initialize_pot(self):
        for player in self.__players:
            if player.ante():
                self.__pot.add_one_coin()


    # ----------------------------------------------------------------- output
    def show_players(self):
        for player in self.__players:
            print(player)

    def __print_round_summary(self):
        print("\n--- Round Summary ---")
        active = [p for p in self.__players if p.is_active()]
        eliminated = [p for p in self.__players if not p.is_active()]
        for player in active:
            print(player)
        for player in eliminated:
            print(f"{player}  (eliminated)")
        print(self.__pot)
        print("---------------------\n")


    # ------------------------------------------------------------------- main
    def play(self):
        print(f"\nGame begins! with:")
        self.show_players()
        print()

        for rnd in range(1, self.__rounds + 1):
            # spec 5: announce the last round before it is played
            if rnd == self.__rounds:
                print("*** This is the LAST round! ***")

            self.__play_round(rnd)

            # stop early if only one (or zero) players remain
            if len([p for p in self.__players if p.is_active()]) <= 1:
                break

        self.__announce_winner()
    # --------------------------------------------------------------- end main

    # ------------------------------------------------------- helper functions
    def __play_round(self, round_number):
        print(f"\n========== Round {round_number} ==========")
        # only active players take a turn
        active_players = [p for p in self.__players if p.is_active()]
        for player in active_players:

            print(player)
            self.__player_take_turn(player, round_number)
        self.__print_round_summary()

    # ------new methoud pot check---------

    def __pot_check(self,current_pot):
        if current_pot.get_coins() < 2:
            self.__initialize_pot()



    #--------------------------------------
    def __player_take_turn(self, player, round_number):
        if player.get_coins() > 0:
            coins_eaten = self.__eat_coins(player)
            if player.get_coins() > 0:
                self.__ante(player)
                #       spin player's dreidel
                side_up = player.spin()
                print(f"player {player.get_name()} spun {side_up}")
                #       adjust pot and player
                self.__adjust_pot_player(player, side_up)
                print(f"after dreidel spin player has {player.get_coins()} coins")
                self.__pot_check(self.__pot)



    def __ante(self,player):
        player.ante()
        self.__pot.add_one_coin()

    #("shin", "gimel", "hey", "nun")
    def __adjust_pot_player(self, player, side_up):
        if side_up == "gimel":
            player.add_coins(self.__pot.payout_gimel())
        elif side_up == "hey":
            player.add_coins(self.__pot.payout_hey())
        elif side_up == "shin":
            player.ante()
            self.__pot.add_one_coin()


    def __eat_coins(self,player):
        coins_eat = get_integer("how many coins would you like to eat?", player.get_coins(), 0 )
        if coins_eat > 0:
            player.eat(coins_eat)

        return coins_eat



    def __announce_winner(self):
        print("\n========== GAME OVER ==========")
        # spec 6: winner is the player who ate the most chocolate coins
        # TO DO finish this function
        # go throgh winners
        # see who was not eliminated but has the lesat amount of coins
        winner_amount = 0
        winner = ""
        for player in self.__players:
            if player.is_active():
                if player.get_eaten_coins() > winner_amount:
                    winner = player.get_name()
                    winner_amount = player.get_eaten_coins()
        if winner_amount > 0:
            print(f"\n{winner} wins with {winner_amount} coins eaten!")
        else:
            print("no winner all players were eliminated \n play again!")






if __name__ == "__main__":
    def start_game():
        game = Game()
        game.play()


    start_game()