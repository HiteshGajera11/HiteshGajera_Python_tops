"""Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle"""

class Rectangle():
    def _init_(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())