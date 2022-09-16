import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
'''
# higher order functions that take in other functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def calculator(n1, n2, compute):
    return compute(n1, n2)


print(f"addition: {calculator(5, 3, add)}")
print(f"subtract: {calculator(7, 2, subtract)}")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.setheading(tim.heading()+10)


def clockwise():
    tim.setheading(tim.heading()-10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "W")
screen.onkey(move_backwards, "S")
screen.onkey(counter_clockwise, "A")
screen.onkey(clockwise, "D")
screen.onkey(clear_drawing, "C")
screen.exitonclick()


'''
# understanding the Turtle coordinate system

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -30, 10, 50, 90, 130]
all_turtles = []


def turtles():
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)


turtles()

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
