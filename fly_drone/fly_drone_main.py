from drone import Drone


def main():
    drone1 = Drone()
    option = 5
    while option != 0:
        option = int(input("Enter 1 for accelerate, 2 for decelerate,"
                           "3 for ascend, 4 for descend, 0 to exit: "))
        if option == 1:
            drone1.accelerate()
            print("Speed: ", drone1.speed, "Height: ", drone1.height)
        elif option == 2:
            drone1.decelerate()
            print("Speed: ", drone1.speed, "Height: ", drone1.height)
        elif option == 3:
            drone1.ascend()
            print("Speed: ", drone1.speed, "Height: ", drone1.height)
        elif option == 4:
            drone1.descend()
            print("Speed: ", drone1.speed, "Height: ", drone1.height)


main()
