from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self, base, height):
        print(f"The area of the triangle is {0.5 * base * height}")

class Rectangle(Shape):
    def area(self, width, height):
        print(f"The area of the rectangle is {width * height}")  

class Square(Shape):
    def area(self, side):
        print(f"The area of the square is {side * side}")    
square = Square()
triangle = Triangle()
rectangle = Rectangle()
square.area(4)
triangle.area(5, 6)
rectangle.area(7, 8)
