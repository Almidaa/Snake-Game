# Simple Snake Game
#thx TokyoEdThec
#Part 1: Getting Started

import turtle
import time

delay = 0.5
points = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Almeida")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) #when 0, screen updates turn off

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "left"
head.onscreenclick(lambda x, y: turtle.goto(x, y) or print(turtle.xcor(), turtle.ycor())

#Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)


def increment_points():
    global points
    points += 1

#Main Gme loop


while points < 10:
    wn.update()

    move()
    increment_points()
    print(head.position())
    time.sleep(delay)

wn.mainloop()

