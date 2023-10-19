from turtle import Turtle,Screen

myTurtle = Turtle()
myScreen = Screen()

def moveForward():
    myTurtle.forward(20)

def moveBackward():
    myTurtle.backward(20)

def counterClock():
    myTurtle.left(10)

def clockWise():
    myTurtle.right(10)

def clearDrawing():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.home()
    myTurtle.pendown()

# etch a sketch

myScreen.listen()
myScreen.onkey(key="w", fun=moveForward)
myScreen.onkey(key="s", fun=moveBackward)
myScreen.onkey(key="a", fun=counterClock)
myScreen.onkey(key="d", fun=clockWise)
myScreen.onkey(key="c", fun=clearDrawing)

myScreen.exitonclick()