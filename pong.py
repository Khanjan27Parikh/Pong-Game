import turtle
from Game_objects import *
from Score import *
import winsound

wn = turtle.Screen()
wn.title("Pong by Khanjan Parikh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# For sound in windows 
# 1. import winsound, winsound.PlaySound("filename", winsound.SND_ASYNC)


# Function
# For Paddle A
def paddle_a_up():
 y = paddle_a.ycor()
 y += 20
 paddle_a.sety(y)

def paddle_a_down():
 y = paddle_a.ycor()
 y -= 20
 paddle_a.sety(y)

# For Paddle B
def paddle_b_up():
 y = paddle_b.ycor()
 y += 20
 paddle_b.sety(y)

def paddle_b_down():
 y = paddle_b.ycor()
 y -= 20
 paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
 wn.update()

 # Movement for ball
 ball.setx(ball.xcor() + ball.dx)
 ball.sety(ball.ycor() + ball.dy)

 # Border checking
 # top
 if ball.ycor() > 290:
  ball.sety(290)
  ball.dy *= -1
  winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)

 # bottom
 if ball.ycor() < -290:
  ball.sety(-290)
  ball.dy *= -1
  winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)

 # right side
 if ball.xcor() > 390:
  ball.goto(0, 0)
  ball.dx *= -1
  score_a += 1 
  pen.clear()
  pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
            font=("Courier", 24, "normal"))
  winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)

 # left side
 if ball.xcor() < -390:
  ball.goto(0, 0)
  ball.dx *= -1
  score_b += 1
  pen.clear()
  pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
            font=("Courier", 24, "normal"))
  winsound.PlaySound("pong_sound.wav", winsound.SND_ASYNC)

 # Paddle and Ball collisions
 # For Paddle B
 if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
  ball.setx(340)
  ball.dx *= -1
  winsound.PlaySound("pong_sound1.wav", winsound.SND_ASYNC)

 # For Paddle A
 if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
  ball.setx(-340)
  ball.dx *= -1
  winsound.PlaySound("pong_sound1.wav", winsound.SND_ASYNC)
