from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake  Game")
screen.tracer(0)

snake=Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        is_game_on=False
        score.game_over()

    #Detect collision with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            is_game_on=False
            score.game_over()


screen.exitonclick()