from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if not -280 <= snake.head.xcor() <= 280 or not -280 <= snake.head.ycor() <= 280:
        game_on = False
        scoreboard.game_over()

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
