import math

class Shape:
    def area(self):
        # Base method, intended to be overridden in derived classes
        raise NotImplementedError("Subclasses must override this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override area method to compute the area of a rectangle
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override area method to compute the area of a circle
        return math.pi * self.radius ** 2
