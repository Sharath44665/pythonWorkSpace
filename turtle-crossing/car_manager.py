COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from scoreboard import Scoreboard
import random
class CarManager(Scoreboard):
    def __init__(self):
        super().__init__()
        self.allCars = []



    def createCar(self):

        # if dice == 1 only then create cars
        dice = random.randint(1,6)
        if dice == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            userColor = random.choice(COLORS)
            ypos= random.randint(-250, 250)
            car.color(userColor)
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.goto(x=300,y=ypos)
            self.allCars.append(car)

    # def move(self,level =0):
    #     for car in self.allCars:
    #         car.backward(MOVE_INCREMENT)
    #         if level == 0:
    #             car.speed("normal")
    #         elif level == 1:
    #             car.speed("fast")
    #         else:
    #             car.speed("fastest")
    #     self.createLevelText(level=level)
        # self.car.backward(10)

    def move(self,level = 0):
        carSpeed = 0
        if level == 0:
            carSpeed = MOVE_INCREMENT
        else:
            carSpeed = (level+1)*MOVE_INCREMENT

        # print(f"car speed: {carSpeed}")
        for car in self.allCars:
            car.backward(carSpeed)
        self.createLevelText(level=level)

