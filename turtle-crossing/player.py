STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player:
    def __init__(self):
        self.newTurle = Turtle()

    def getPlayer(self):
        return self.newTurle

    def createTurtle(self):

        self.newTurle.shape("turtle")
        self.newTurle.penup()
        self.newTurle.color("red")
        self.newTurle.goto(x=STARTING_POSITION[0], y= STARTING_POSITION[1])
        self.newTurle.left(90)

    def getyPosition(self):
        return self.newTurle.ycor()


    def moveStartingPos(self):
        self.newTurle.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
    def moveUp(self):
        self.newTurle.forward(10)

    def moveDown(self):
        self.newTurle.backward(10)
