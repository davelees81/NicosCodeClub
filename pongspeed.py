import turtle
import os

from ast import Str
from pickle import TRUE
from turtle import width


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=10, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=2.5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24,"normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 295:
        ball.sety(295)
        ball.dy *= -1

    if ball.ycor() < -295:
        ball.sety(-295)
        ball.dy *= -1

    if ball.xcor() > 395:
        ball.goto(0, 0)
        # ball.dx *= -1
        ball.dx = -0.1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))


    if ball.xcor() < -395:
        ball.goto(0, 0)
        # ball.dx *= -1
        ball.dx = 0.4
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))



    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 25 and ball.ycor() > paddle_b.ycor() - 25 :
        ball.dx = -0.1
        # os.system("play Ping-pong-ball-bounce-sound-effect.mp3&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() > paddle_a.ycor() - 100 and ball.ycor() < paddle_a.ycor() + 100 :
        ball.dx = 0.4
        # os.system("play Ping-pong-ball-bounce-sound-effect.mp3&")

    


