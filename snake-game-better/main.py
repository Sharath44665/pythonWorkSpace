import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

myScreen = Screen()
myScreen.setup(height=600, width=600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")
myScreen.tracer(0) # turn off the tracer

snake = Snake()
snakeHead = snake.snakeList[0]
myScreen.onkey(fun=snake.moveUp, key="Up")
myScreen.onkey(fun=snake.moveLeft, key="Left")
myScreen.onkey(fun=snake.moveDown, key="Down")
myScreen.onkey(fun=snake.moveRight, key="Right")

getFood = Food()
myScreen.listen()
isGameOn = True
score = ScoreBoard()

getFood.changePosition()

while isGameOn:
    myScreen.update()
    time.sleep(0.1)
    snake.move()

    # print(f"snake position:{snakeHead.position()}")
    # detect food
    if snakeHead.distance(getFood)<15:
        getFood.changePosition()
        # increase length of snake
        snake.increaseLength()
        # update score
        score.increaseScore()
    # print(f"head position: {snakeHead.position()}")
    # detect collision with wall:
    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < -290:
        # score.gameOver()
        score.reset()
        snake.reset()
        snakeHead = snake.snakeList[0]
        # isGameOn = False

    for singleSnake in snake.snakeList[1:]:
        if singleSnake.distance(snakeHead) < 8:
            # print(f"distance: {snakeHead.distance(singleSnake)}")
            # isGameOn = False
            # score.gameOver()
            score.reset()
            snake.reset()
            snakeHead = snake.snakeList[0]



    # for singleSnake in snake.snakeList:
    #     if snakeHead == singleSnake:
    #         pass
    #     elif snakeHead.distance(singleSnake) < 10:
    #         isGameOn = False
    #         score.gameOver()

    # print(snakeHead.xcor())



myScreen.exitonclick()