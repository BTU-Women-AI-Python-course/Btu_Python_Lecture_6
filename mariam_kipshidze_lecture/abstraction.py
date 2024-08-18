from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Creating instances of Rectangle and Circle
rect = Rectangle(5, 10)
circ = Circle(7)

print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 50
print("Rectangle Perimeter:", rect.perimeter())  # Output: Rectangle Perimeter: 30
print("Circle Area:", circ.area())  # Output: Circle Area: 153.86
print("Circle Perimeter:", circ.perimeter())  # Output: Circle Perimeter: 43.96
