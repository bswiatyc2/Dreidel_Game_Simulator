from dreidel import Dreidel


class Player:

    def __init__(self, name, dreidel):
        self.__name = name
        self.__dreidel = dreidel
        self.__number_of_coins = 0
        self.__eaten_coins = 0

    def __str__(self):
        return f"{self.__name} has {self.__number_of_coins} coins"

    # ---------------------------------------------------------------- getters

    def get_name(self):
        return self.__name

    def get_coins(self):
        return self.__number_of_coins

    def get_eaten_coins(self):
        return self.__eaten_coins

    # ----------------------------------------------------------- game actions

    def eat(self, coins):
        if coins <= self.__number_of_coins:
            self.__number_of_coins -= coins
            self.__eaten_coins += coins
        else:
            print(f"you don't have {coins} coins")
            print("no action taken")

    def spin(self):
        self.__dreidel.spin()
        return self.__dreidel.get_sideup()

    def add_coins(self, count):
        self.__number_of_coins += count

    def ante(self):
        anted = 0
        if self.__number_of_coins >= 1:
            anted = 1
            self.__number_of_coins -= 1
        return anted

    def is_active(self):
        return self.__number_of_coins > 0


if __name__ == "__main__":
    dreidel = Dreidel("red")
    player = Player('Ayelet', dreidel)
    print(player)
    player.add_coins(5)
    print(f"Ayelet got 5 coins: {player}")

