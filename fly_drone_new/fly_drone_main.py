from drone import Drone


def main():
    drone1 = Drone()
    option = 5
    while option != 0:
        option = int(input("Enter 1 for accelerate, 2 for decelerate,"
                           "3 for ascend, 4 for descend, 0 to exit: "))
        if option == 1:
            drone1.accelerate()
            print(drone1)
        elif option == 2:
            drone1.decelerate()
            print(drone1)
        elif option == 3:
            drone1.ascend()
            print(drone1)
        elif option == 4:
            drone1.descend()
            print(drone1)


main()
