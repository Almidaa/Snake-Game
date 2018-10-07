# Simple Snake Game
#thx TokyoEdThec

import turtle
import time
import random

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
                   
# Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)  # Needs to be corrected. Initial postiion should be random and not (0, 100)
                   
segments = []

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
                   
 def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"                  
                   
 # Keyboard binds

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")                  




# Main Game loop

while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear the segments list
        segments.clear()

    move ()

    # Collsion with the food
    if head.distance(food) < 20:
        # Move the food to a random spot on the screnn
        x=random.randint(-290, 290)
        y=random.randint(-290, 290)
        food.goto(x, y)

        #New segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        segments[0].color("white")

    # Move the end segments first in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
           
    time.sleep(delay)

wn.mainloop()
