from course import Course


def main():
    course_code = input("Enter course code: ").upper()
    max_class_size = int(input("Enter maximum class size: "))
    course1 = Course(course_code, max_class_size)

    option = 5
    while option != 0:
        option = int(input("Enter 1 to add student, 2 to drop student, "
                           "3 for class info, 4 for change maximum class size, 0 to exit: "))
        if option == 1:
            course1.add_student()
        elif option == 2:
            course1.drop_student()
        elif option == 3:
            print("Course code: ", course1.getCourseCode(), "\nMaximum class size: ", course1.getMaxClassSize(),
                  "\nEnrollment: ", course1.getEnrollment())
        elif option == 4:
            max_class_size = int(input("Enter new maximum class size: "))
            course1.setMaxClassSize(max_class_size)


main()
