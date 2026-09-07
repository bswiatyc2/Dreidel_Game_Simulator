"""
Dreidel class for the dreidel coin game — see README.md for full game rules.

Represents a single dreidel that can be spun to land on one of four sides:
nun, gimel, hey, shin
"""
import random


class Dreidel:
    __SIDES = ("shin", "gimel", "hey", "nun")

    def __init__(self, color):
        self.__sideup = "spinning"
        self.__color = color

    def __str__(self):
        return str(self.__color) + " dreidel shows " + self.__sideup

    # ---------------------------------------------------------------- getters
    def get_sideup(self):
        return self.__sideup

    def get_color(self):
        return self.__color

    # ---------------------------------------------------------------- action
    def spin(self):
        self.__sideup = random.choice(self.__SIDES)




if __name__ == "__main__":
    # test Dreidel
    #random.seed(123456)
    color = input("what color is your dreidel? ")
    svivon = Dreidel(color)
    mean = Dreidel("BLACK")

    print("svivon: ", svivon)
    print("mean dreidel", mean)
    svivon.spin()
    print("after a spin")
    print(svivon)

    spin = 0
    while mean.get_sideup() != 'gimel':
        mean.spin()
        spin += 1
        print("spin ", spin)

    print("svivon: ", svivon)
    print("mean dreidel", mean)


