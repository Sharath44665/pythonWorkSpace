import turtle
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("US states Games")
usImg = "blank_states_img.gif"
screen.addshape(usImg)

myTurtle = Turtle()
myTurtle.shape(usImg)
myTurtle.penup()

statesData = pandas.read_csv("50_states.csv")
allStateList = statesData.state.tolist()
writeTurtle = Turtle()
writeTurtle.hideturtle()
writeTurtle.penup()
isEnterState = True
userEnteredState = {}
rightCounter = 0
notStateList = []
# bugs:
# 1. what to do, if user entered same input text more than once? = fixed
# 2. how to get a text from the screen? = used another way to fix this issue and fixed

while isEnterState:
    stateName = screen.textinput(title=f" right states: {rightCounter}/50 ", prompt="Please enter the sate name: ").title()
    stateName = stateName.strip()

    # get the row
    if stateName in allStateList:
        row = statesData[statesData.state == stateName]
        # print(row)
        # get the row idx
        # print(row.index)

        # get the column names
        # print(row.columns)
        # get the rowIdx
        rowIdx = int(row.index[0])
        # print(rowIdx)
        # get the x coordintate
        xValue = row.at[rowIdx,"x"]
        yValue = row.at[rowIdx, "y"]
        # print(type(xValue))
        xValue = int(xValue)
        yValue = int(yValue)
        writeTurtle.goto(x=xValue,y=yValue)
        writeTurtle.write(stateName,align="center",font=('Arial', 12, 'normal'))
        if stateName not in userEnteredState:
            rightCounter += 1
        userEnteredState[stateName] = [xValue,yValue]
    if stateName == "Exit":
        break
for state in allStateList:
    if state not in userEnteredState:
        notStateList.append(state)

notEntered ={
    "not entered states" : notStateList
}

makeCSV = pandas.DataFrame(notEntered)
makeCSV.to_csv("not entered states.csv")




# rowValues = row.values
# mylist = list(rowValues[0])
# print(mylist)







# getting x y coordinates of the screen
# def getMouseClickCoOrdinate(x,y):
#     print(x,y)
#
# # myTurtle.onscreenclick()
# myTurtle.onclick(fun=getMouseClickCoOrdinate,)

# screen.mainloop()
# screen.exitonclick()