from turtle import Turtle,Screen

myTurtle = Turtle()
myTurtle.shape("turtle")

# draw square:

# myTurtle.forward(100)
# for _ in range(3):
#     myTurtle.right(90)
#     myTurtle.forward(100)

# drawing dashed line:

# for x in range(10):
#
#     myTurtle.forward(10)
#     myTurtle.penup()
#     myTurtle.forward(10)
#     myTurtle.pendown()

# drawing shapes
myScreen = Screen()
import random
totalSize = 360

myScreen.colormode(255)
for x in range(3,9):
    getAngle = totalSize // x


    for _ in range(0,x):
        myTurtle.forward(100)
        myTurtle.right(getAngle)

    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)

    myTurtle.pencolor(red,blue,green)



myScreen.exitonclick()