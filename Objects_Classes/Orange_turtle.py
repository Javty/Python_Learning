import turtle

class BigOrangeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.width(10)
        self.forward(100)

ramon = BigOrangeTurtle()
