FONT = ("Courier", 18, "normal")

from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        pass

    def createLevelText(self,level):
        self.turtle.penup()
        self.turtle.goto(x=-270,y=250)
        self.turtle.clear()
        self.turtle.write(f"Level: {level}", align='left', font=FONT)

    def gameOver(self):
        self.turtle.write(f"Game Over!!!", align='center', font=FONT)

    pass
