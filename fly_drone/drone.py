#  define class Drone with the following 5 methods: init, accelerate, decelerate
#  ascend, descend


class Drone:

    def __init__(self):

        """ constructor of class Drone """

        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        speed = 10
        self.speed = self.speed + speed

    def decelerate(self):
        speed = 10
        if self.speed < 10:
            print("The drone speed cannot be negative.")
        else:
            self.speed = self.speed - speed

    def ascend(self):
        height = 10
        self.height = self.height + height

    def descend(self):
        height = 10
        if self.height < 10:
            print("The new height cannot be negative.")
        else:
            self.height = self.height - height


