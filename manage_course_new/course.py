class Course:

    def __init__(self, course_code, max_class_size):

        """ constructor for class Course """

        self.__course_code = course_code
        self.__max_class_size = max_class_size
        self.__enrollment = 0

    def add_student(self):
        enrollment = 1
        if self.__enrollment >= self.__max_class_size:
            print("Sorry! Course already full. \nEnrollment: ", self.__enrollment)
        else:
            self.__enrollment = self.__enrollment + enrollment
            print("One student added. \nEnrollment: ", self.__enrollment)

    def drop_student(self):
        enrollment = 1
        if self.__enrollment == 0:
            print("Course is empty")
        else:
            self.__enrollment = self.__enrollment - enrollment
            print("One student dropped. \nEnrollment: ", self.__enrollment)

    def getCourseCode(self):
        return self.__course_code

    def getMaxClassSize(self):
        return self.__max_class_size

    def getEnrollment(self):
        return self.__enrollment

    def setMaxClassSize(self, max_class_size):
        if max_class_size < 0:
            print("New maximum class size cannot be negative.")
        elif max_class_size < self.__enrollment:
            print("New maximum class size cannot be less than current enrollment.")
        else:
            self.__max_class_size = max_class_size
            print("Maximum class size changed.")
