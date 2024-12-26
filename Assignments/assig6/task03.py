from abc import ABC, abstractmethod
import tkinter as tk

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas, x, y):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self, canvas, x, y):
        canvas.create_rectangle(x, y, x + self.width, y + self.height, outline="black")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def draw(self, canvas, x, y):
        canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, outline="black")

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Oval(Circle):
    def __init__(self, radius, vertical_radius):
        super().__init__(radius)
        self.vertical_radius = vertical_radius

    def area(self):
        return 3.14 * self.radius * self.vertical_radius


window = tk.Tk()
window.title("Shapes Drawing")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


rectangle = Rectangle(50, 30)
circle = Circle(25)
square = Square(40)
oval = Oval(30, 20)


rectangle.draw(canvas, 50, 50)
circle.draw(canvas, 200, 50)
square.draw(canvas, 50, 200)
oval.draw(canvas, 200, 200)


window.mainloop()
