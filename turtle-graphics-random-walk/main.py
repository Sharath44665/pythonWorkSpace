from turtle import Turtle,Screen
import random

myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)
direction = [0,90,180,270]

myTurtle.pensize(10)
for _ in range(100):
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    myTurtle.pencolor(red, green, blue)
    myTurtle.setheading(random.choice(direction))
    myTurtle.forward(40)


myScreen.exitonclick()