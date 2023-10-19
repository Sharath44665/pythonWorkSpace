from turtle import Turtle,Screen
import colorgram
import random


# colors = colorgram.extract("paint.jpg", 12)
# # firstColor = colors[0]
# # rgb = firstColor.rgb
# # red = rgb[0]
# # green = rgb[1]
# # blue = rgb[2]
# # print(red)
# # print(green)
# # print(blue)
#
listOfColors = [{'red': 198, 'green': 175, 'blue': 119}, {'red': 125, 'green': 36, 'blue': 23}, {'red': 187, 'green': 157, 'blue': 50}, {'red': 170, 'green': 104, 'blue': 56}, {'red': 5, 'green': 56, 'blue': 83}, {'red': 201, 'green': 216, 'blue': 205}, {'red': 109, 'green': 67, 'blue': 85}, {'red': 39, 'green': 35, 'blue': 34}, {'red': 223, 'green': 224, 'blue': 227}, {'red': 84, 'green': 141, 'blue': 61}]
#
# for idx in range(2, len(colors)):
#     color = colors[idx]
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#
#     listOfColors.append({
#         "red": red,
#         "green":green,
#         "blue":blue
#                          })
# print(listOfColors)

myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)
myTurtle.penup()
xPosition = -200
yPosition = -300
myTurtle.setpos(x=xPosition, y=yPosition)
for _ in range(10):

    for _ in range(10):
        colorChoice = random.choice(listOfColors)
        red = colorChoice["red"]
        blue = colorChoice["blue"]
        green = colorChoice["green"]

        myTurtle.pencolor(red, blue, green)
        myTurtle.pendown()
        myTurtle.dot(20)
        myTurtle.penup()
        myTurtle.forward(50)
    yPosition += 50
    myTurtle.setpos(x=xPosition, y=yPosition)



myScreen.exitonclick()