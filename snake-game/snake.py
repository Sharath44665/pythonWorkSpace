from turtle import Turtle
MOVE_DISTANCE = 10
LEFT = 180
RIGHT = 0
DOWN = 270
UP = 90
class Snake:
    def __init__(self):
        self.snakeList = []
        self.createDefaultSnake()


    def createDefaultSnake(self):
        xCordinate = 0
        yCordinate = 0
        for _ in range(3):
            newTurtle = Turtle()
            newTurtle.shape("square")
            newTurtle.color("white")
            newTurtle.penup()
            newTurtle.goto(x= xCordinate, y=yCordinate)
            xCordinate -= 20
            self.snakeList.append(newTurtle)


    def increaseLength(self):

        tailSnake = self.snakeList[len(self.snakeList)-1]
        tailSnakePosition = tailSnake.position()
        # print(tailSnakePosition)
        xCordinate = tailSnakePosition[0]
        yCordinate = tailSnakePosition[1]
        newTurtle = Turtle()
        newTurtle.penup()
        newTurtle.shape("square")
        newTurtle.color("white")
        # xCordinate -= 20
        newTurtle.goto(x=xCordinate, y=yCordinate)
        self.snakeList.append(newTurtle)


    def move(self):
        for idx in range(len(self.snakeList)-1, 0, -1):
            newPosition = self.snakeList[idx-1].position()
            xPos = newPosition[0]
            yPos = newPosition[1]

            self.snakeList[idx].goto(x=xPos,y=yPos)
        self.snakeList[0].forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.snakeList[0].heading() != DOWN:
            self.snakeList[0].setheading(UP)

    def moveLeft(self):
        if self.snakeList[0].heading() != RIGHT:
            self.snakeList[0].setheading(LEFT)

    def moveDown(self):
        # print()
        if self.snakeList[0].heading() != UP:
            self.snakeList[0].setheading(DOWN)

    def moveRight(self):
        if self.snakeList[0].heading() != LEFT:
            self.snakeList[0].setheading(RIGHT)


   

