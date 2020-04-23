#  define class Drone with the following 5 methods: init, accelerate, decelerate
#  ascend, descend


class Drone:

    def __init__(self):

        """ constructor of class Drone """

        self.__speed = 0
        self.__height = 0

    def accelerate(self):
        speed = 10
        self.__speed = self.__speed + speed

    def decelerate(self):
        speed = 10
        if self.__speed < 10:
            print("The drone speed cannot be negative.")
        else:
            self.__speed = self.__speed - speed

    def ascend(self):
        height = 10
        self.__height = self.__height + height

    def descend(self):
        height = 10
        if self.__height < 10:
            print("The drone height cannot be negative.")
        else:
            self.__height = self.__height - height


    def __str__(self):
        return "Speed: " + str(self.__speed) + " Height: " + str(self.__height)
