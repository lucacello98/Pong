from turtle import Turtle

class Ball(Turtle):
    # Initialize the ball with position and movement speed
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1, 1)
        self.goto(x_pos, y_pos)
        self.x_move = 3
        self.y_move = 3

    # Move the ball based on its speed
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Reverse the ball's direction on the y-axis
    def bounce_y(self):
        self.y_move *= -1

    # Reverse the ball's direction on the x-axis
    def bounce_x(self):
        self.x_move *= -1

    # Reset the ball to the center of the screen
    def game_reset(self):
        self.goto(0, 0)
        self.bounce_x()



