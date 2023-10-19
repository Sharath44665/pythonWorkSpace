from turtle import Turtle,Screen
import random

demoTurtle = Turtle()
myscreen = Screen()

myscreen.colormode(255)

demoTurtle.speed("fastest")
for angle in range(0,360,10):
    demoTurtle.setheading(angle)
    demoTurtle.circle(100)
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    demoTurtle.pencolor(red,green,blue)

myscreen.exitonclick()
