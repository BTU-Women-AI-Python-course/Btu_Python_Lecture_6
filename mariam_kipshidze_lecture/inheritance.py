class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} My student ID is {self.student_id}."


student = Student("Alice", 21, "S12345")
print(student.introduce())

# Output: My name is Alice and I am 21 years old. My student ID is S12345.
