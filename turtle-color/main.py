import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("#a0c8f0")

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(10)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for i in range(100):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
