class Course:

    def __init__(self, course_code, max_class_size):

        """ constructor for class Course """

        self.course_code = course_code
        self.max_class_size = max_class_size
        self.enrollment = 0

    def add_student(self):
        enrollment = 1
        if self.enrollment >= self.max_class_size:
            print("Course already full")
        else:
            self.enrollment = self.enrollment + enrollment
            print("One student added. \nEnrollment: ", self.enrollment)

    def drop_student(self):
        enrollment = 1
        if self.enrollment == 0:
            print("Course is empty")
        else:
            self.enrollment = self.enrollment - enrollment
            print("One student dropped. \nEnrollment: ", self.enrollment)

