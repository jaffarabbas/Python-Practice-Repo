# Write a Rectangle class in Python language, allowing you to build a rectangle with length 
# and width attributes.Create a Perimeter() method to calculate the perimeter of the rectangle
# and a Area() method to calculate the area of ​​the rectangle.Create a method display() that 
# display the length, width, perimeter and area of an object created using an instantiation on 
# rectangle class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Perimeter: ", self.Perimeter())
        print("Area: ", self.Area())

r = Rectangle(10, 20)
r.display()

