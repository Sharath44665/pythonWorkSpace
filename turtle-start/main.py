# from turtle import Turtle,Screen
#
# myTurtle = Turtle()
# myTurtle.shape("turtle")
# myTurtle.color("coral")
#
# myScreen = Screen()
# myTurtle.forward(100)
#
#
# myScreen.exitonclick()

from prettytable import PrettyTable
# using pretty table
table = PrettyTable()
# print(table)

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

# print(table)

table.align = "l"
print(table)

