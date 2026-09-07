"""
this is a draidel game craeted as part of an asinment in an advavanced python class:

THE GOAL:
    crate a draeidal class in wich we can simulate a game of draidel

RULES OF THE GAME:

"""
import random


class Dreidel:
    __sides = ("shin", "gimel", "hey", "nun")

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
        #side_up = random.randint(0, 3)
        #self.__sideup = self.__sides[side_up]
        self.__sideup = random.choice(self.__sides)




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

# print("my dreidel calls .get_color():", svivon.get_color())
# for turn in range(1, 21):
#     svivon.spin()
#     print(f"turn {turn}: {svivon}")
