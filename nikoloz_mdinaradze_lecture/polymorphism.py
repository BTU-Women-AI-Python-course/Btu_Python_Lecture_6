import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        sqr = self.x**2+self.y**2
        return math.sqrt(sqr)


class Distance:
    def __init__(self, end, start=0):
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

point1 = Point(3,4)
print(point1.length())

distance1 = Distance(5, 1)
print(distance1.length())
