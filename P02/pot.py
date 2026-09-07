class Pot:

    def __init__(self):
        self.__number_of_coins = 0

    # ___str method _____________________________

    def __str__(self):
        return f"the pot currently has {self.__number_of_coins}"


    # ---------------------------------------------------------------- action
    def add_one_coin(self):
        self.__number_of_coins += 1

    def payout_gimel(self):
        number = self.__number_of_coins
        self.__number_of_coins = 0
        return number

    def payout_hey(self):
        number = self.__number_of_coins // 2
        self.__number_of_coins -= number
        return number

    def get_coins(self):
        return self.__number_of_coins
