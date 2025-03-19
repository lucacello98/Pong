from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen and its properties
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating paddles, ball, and scoreboard
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball(0, 0)
scoreboard = Scoreboard()

# Listening for key presses to control paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.01)  # Controls game speed
    screen.update()   # Update screen
    ball.move()       # Move the ball

    # Bounce ball when it hits the top or bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Reset ball and update score when the ball crosses the right boundary
    if ball.xcor() > 400:
        time.sleep(1)  # Delay for reset
        ball.game_reset()
        scoreboard.l_point()  # Left player scores

    # Reset ball and update score when the ball crosses the left boundary
    if ball.xcor() < -420:
        time.sleep(1)  # Delay for reset
        ball.game_reset()
        scoreboard.r_point()  # Right player scores

# Close the game when clicked
screen.exitonclick()

