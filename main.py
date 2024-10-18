# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 19 - Intermediate - Python Turtles Race Betting Game
# Classes can have multiple instances and states
# Code was modified for cellphone use (Pydroid 3)
from turtle import Turtle, Screen
import random

is_race_on = False
screen_width = 500
screen_height = 400
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_count = len(colors)

# Create a border for cellphone use (Pydroid 3), since it's in fullscreen mode:
border_turtle = Turtle(shape="turtle")
border_turtle.penup()
border_turtle.speed("slow") # values of slowest, slow, normal, fast and fastest
border_turtle_x = -screen_width/2
border_turtle_y = -screen_height/2
print(border_turtle_x)
border_turtle.goto(x=border_turtle_x, y=border_turtle_y)
border_turtle.pendown()
for _ in range(2):
    border_turtle.forward(screen_width)
    border_turtle.left(90)
    border_turtle.forward(screen_height)
    border_turtle.left(90)
border_turtle.hideturtle()

i = 0
turtles_count_extra = turtles_count + 4 # used to create empty space on top and bottom
spacing = screen_height/turtles_count_extra
turtle_pos = - ((turtles_count - 1) * spacing) / 2 # position starting from bottom
turtles_cult = []
# Create turtles and set their position:
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    turtles_cult.append(new_turtle)
    turtles_cult[i].penup()
    turtles_cult[i].goto(x=-230, y=turtle_pos)
    i += 1
    turtle_pos += spacing

if user_bet:
    is_race_on = True

# Note: turtle size is 40x40
while is_race_on:
    for turtle in turtles_cult:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                screen.textinput(title="You've won!", prompt=f"The {winning_color} turtle is the winner!") # Added for cellphone use
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                screen.textinput(title="You've lost!", prompt=f"The {winning_color} turtle is the winner!") # Added for cellphone use
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
