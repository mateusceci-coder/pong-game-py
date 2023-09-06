from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        self.pendown()
        self.drawLine()


    def drawLine(self):
        for line in range(16):
            self.forward(30)
            self.penup()
            self.forward(20)
            self.pendown()