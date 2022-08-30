from turtle import Turtle, Screen
import random

color_lst = ["red", "orange", "yellow", "green", "blue", "purple"]

# Turtle objects and list below

abena = Turtle(shape="turtle")
lisa = Turtle(shape="turtle")
jeffrey = Turtle(shape="turtle")
sylvia = Turtle(shape="turtle")
rodrick = Turtle(shape="turtle")
mary = Turtle(shape="turtle")

turtle_players = [abena, lisa, jeffrey, sylvia, rodrick, mary]

# Let's set up the dimension for our play screen
screen = Screen()
screen.setup(width=500, height=400)
screen.title("choose a color: red, orange, yellow, green, blue, violet")

# Let create a prompt interface for the user
your_color = screen.textinput(title="Make a bet", prompt="Which color do you think would win")
y_cord = -100
for turtle_player, _color in zip(turtle_players, color_lst):
    turtle_player.color(_color)
    turtle_player.penup()
    turtle_player.goto(x=-230, y=y_cord)
    turtle_player.showturtle()
    y_cord += 30

game_on = True
while game_on:
    for player in turtle_players:
        player.forward(random.randint(1, 10))
        if player.xcor() > 230:
            print(f"you selected {your_color}")
            winning_color = player.color()
            if your_color.lower() == winning_color[0]:
                print("You won! :)")
            else:
                print("You lost :(")
            print(f"the winning color was {winning_color[0]}")
            game_on = False

screen.exitonclick()

