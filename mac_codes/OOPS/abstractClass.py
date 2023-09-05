from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating instances of the concrete subclasses
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# Calling the area method
print("Circle area:", circle.area())         # Output: Circle area: 78.5
print("Rectangle area:", rectangle.area())   # Output: Rectangle area: 24
