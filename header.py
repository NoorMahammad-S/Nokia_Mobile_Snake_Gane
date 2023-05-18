from turtle import Turtle


class Header(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.shapesize(stretch_wid=0.2, stretch_len=100)

