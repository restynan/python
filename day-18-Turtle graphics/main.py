import turtle as t
# timmy = t.Turtle()
import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
'''
#draw a square
for _ in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


#draw a dashed line
for _ in range(4):
    timmy_the_turtle.forward(10) 
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()





# drawing triangle, square, pentagon, hexagon, heptagon, octagon,nonagon and a decagon

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)


for sides in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# create a random walk
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for _ in range(100):
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(40)

# cannot change items in a tuple once created
my_tuple = (1, 3, 4)

# convert a tuple to a list
list(my_tuple)


'''
# Draw a spirograph
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy_the_turtle.speed("fastest")


def draw_spiral_graph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_spiral_graph(10)

screen = Screen()
screen.exitonclick()
