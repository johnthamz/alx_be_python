import math  # Import math module for using math.pi

# Base class
class Shape:
    def area(self):
        """
        This is a base method that should be overridden by derived classes.
        If not overridden, it raises a NotImplementedError.
        """
        raise NotImplementedError("Subclasses must override this method.")


# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Constructor for Rectangle.
        It initializes the length and width attributes.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides Shape's area() method to compute rectangle area.
        Formula: length × width
        """
        return self.length * self.width


# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        """
        Constructor for Circle.
        It initializes the radius attribute.
        """
        self.radius = radius

    def area(self):
        """
        Overrides Shape's area() method to compute circle area.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
