class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade >= 0 and grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def display_info(self):
        return f"Student: {self.__name}, Grade: {self.__grade}"


# Creating an instance of Student
student = Student("John", 85)

# Accessing and modifying private attribute using methods
print(student.display_info())  # Output: Student: John, Grade: 85
student.set_grade(95)
print(student.display_info())  # Output: Student: John, Grade: 95

# Trying to assign an invalid grade
student.set_grade(110)  # Output: Invalid grade. Must be between 0 and 100.
