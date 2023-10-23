import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level = 0
myTurtle = Player()
myTurtle.createTurtle()
screen.onkey(fun=myTurtle.moveUp, key="Up")
screen.onkey(fun=myTurtle.moveDown, key="Down")

newCar = CarManager()

screen.listen()
game_is_on = True
newLevel = Scoreboard()
# playerSpeed = myTurtle.getPlayer()
while game_is_on:

    time.sleep(0.1)
    newCar.createCar()
    newCar.move(level=level)
    screen.update()

    # succesful cross
    if myTurtle.getyPosition() >= 280:
        myTurtle.moveStartingPos()
        level += 1

#     detect collision
    for car in newCar.allCars:
        if car.distance(myTurtle.getPlayer()) < 20:
            gameOver = Scoreboard()
            gameOver.gameOver()
            game_is_on = False


screen.exitonclick()