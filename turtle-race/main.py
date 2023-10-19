from turtle import Turtle,Screen
import random


myScreen = Screen()
myScreen.setup(height=400,width=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
allTurtle = []

yAxis = -150
xAxis = -220

userColorChoice = myScreen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ").lower()
for idx in range(6):
    myTurtle = Turtle()
    myTurtle.penup()
    myTurtle.shape("turtle")
    myTurtle.color(colors[idx])
    myTurtle.goto(x=xAxis, y=yAxis)
    allTurtle.append(myTurtle)
    yAxis += 40

startRace = False
if userColorChoice in colors:
    startRace = True

while startRace:

    for currentTurtle in allTurtle:
        randomDistance = random.randint(0,10)
        currentTurtle.forward(randomDistance)
        positionOfCurrentTurtle = currentTurtle.position()
        # print(positionOfCurrentTurtle)
        if positionOfCurrentTurtle[0] > 230:
            currentTurtleColor = currentTurtle.color()

            if userColorChoice == currentTurtleColor[0]:
                print(f"your color: {userColorChoice} won! ")
            else:
                print(f"{currentTurtleColor[0]} won, your color : {userColorChoice}")

            startRace = False
            break




myScreen.exitonclick()
