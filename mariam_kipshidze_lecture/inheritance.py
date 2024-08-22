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


""" Multiple inheritance in Python """
class Engine:
    def start_engine(self):
        return "Engine started."

class Radio:
    def play_music(self):
        return "Playing music."

class Vehicle:
    def drive(self):
        return "Driving the vehicle."

class Car(Vehicle, Engine, Radio):
    def start_car(self):
        return "Car is ready to go!"

# Create an instance of Car
my_car = Car()

# Access methods from all parent classes
print(my_car.start_engine())  # Output: Engine started.
print(my_car.play_music())     # Output: Playing music.
print(my_car.drive())          # Output: Driving the vehicle.
print(my_car.start_car())      # Output: Car is ready to go!
