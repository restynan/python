from turtle import Turtle, Screen
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")

def create_snake(x, y):
    for  _ in range(4):
        turtle = Turtle(shape="square")
        turtle.color(color="white")
        turtle.goto(x,y+20)
create_snake(0,0)


screen.exitonclick()