import turtle
from turtle import Turtle


class ScoreBoard():
    def __init__(self):
        self.turtle = Turtle()
        self.score = 0
        self.highScore = 0
        self.turtle.penup()
        # self.turtle.shape(None)
        self.turtle.hideturtle()
        self.turtle.goto(x=0, y=250)
        self.turtle.color("white")
        self.update()
        # self.turtle.write(f"score: {self.score}", align='center', font=('Arial', 12, 'normal'))

    def update(self):
        self.turtle.clear()
        self.turtle.write(f"score: {self.score}", align='center', font=('Arial', 12, 'normal'))

    def increaseScore(self):
        self.score += 1
        self.update()



    def gameOver(self):
        self.turtle.goto(x=0,y=0)
        self.turtle.write("Game Over", align='center', font=('Arial', 12, 'bold'))

        # self.turtle.clear()
        # self.turtle.write(f"Game Over, your total score is: {self.score}", align='center', font=('Arial', 12, 'normal'))




