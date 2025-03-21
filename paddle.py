from turtle import Turtle

class Paddle(Turtle):
    # Initialize paddle with given x position
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x_pos,0)

    # Move paddle up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Move paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
