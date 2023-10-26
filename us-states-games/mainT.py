from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US states Games")
usImg = "blank_states_img.gif"
screen.addshape(usImg)
myTurtle = Turtle()
myTurtle.shape(usImg)
# myTurtle.penup()
stateData = pandas.read_csv("50_states.csv")

isStateEntered = True
stateList = stateData.state.tolist()
userEnteredState ={}
# notEnteredStatesList = []
counter = 0
while isStateEntered:
    stateName = screen.textinput(title=f"{counter}/50 Correct states", prompt="Enter the state name:").title()
    stateName = stateName.strip()

    if stateName in stateList:
        writeTurtle = Turtle()
        writeTurtle.hideturtle()
        writeTurtle.penup()

        stateRow = stateData[stateData.state == stateName]
        # print(stateRow.state.item())
        stateNameFromCSV = stateRow.state.item()

        xValue = int(stateRow.x)
        yValue = int(stateRow.y)
        writeTurtle.goto(x=xValue, y=yValue)
        if stateName not in userEnteredState:
            counter += 1

        userEnteredState[stateNameFromCSV] = [xValue, yValue]
        # writeTurtle.write(stateName,align="center",font=('Arial', 12, 'normal'))
        writeTurtle.write(stateNameFromCSV, align="center", font=('Arial', 12, 'normal'))

    elif stateName == "Exit":

        isStateEntered = False

# for state in stateList:
#     if state not in userEnteredState:
#         notEnteredStatesList.append(state)

notEnteredStatesList = [state for state in stateList if state not in userEnteredState]

notEnteredStates = {"not entered": notEnteredStatesList}
notEntered = pandas.DataFrame(notEnteredStates)
notEntered.to_csv("not entered states.csv")

# screen.exitonclick()
