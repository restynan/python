from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


def create_snake():
    for position in starting_positions:
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.goto(position)


create_snake()

screen.exitonclick()
