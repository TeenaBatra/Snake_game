from turtle import Screen
from snake import *
from food import Food
from scoreboard import ScoreBoard
import time

# creating instances of the modules imported
screen = Screen()
scoreboard = ScoreBoard()
main_snake = Snake()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

main_snake.create_snake_body()
food = Food()

screen.listen()
screen.onkey(main_snake.up, "Up")
screen.onkey(main_snake.down, "Down")
screen.onkey(main_snake.left, "Left")
screen.onkey(main_snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.15)
    main_snake.move()
    # detect collision with food
    if main_snake.head.distance(food) < 15:
        food.refresh()
        main_snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if main_snake.head.xcor() > 290 or main_snake.head.xcor() < -290 or main_snake.head.ycor() > 290 or main_snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    # detect collision with tail
    for segment in main_snake.snake[1:]:
        if main_snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
