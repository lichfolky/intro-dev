# https://docs.python.org/3/library/turtle.html

import turtle
import math

home_size = 500
radius = 20

s = turtle.getscreen()


def draw_room(t):
    t.color("black")
    t.width(3)
    t.up()
    t.goto(-home_size / 2, home_size / 2)
    t.down()
    t.forward(home_size)
    t.right(90)
    t.forward(home_size)
    t.right(90)
    t.forward(home_size)
    t.right(90)
    t.forward(home_size)


def draw_roomba(t):
    t.circle(radius)
    t.circle(radius / 2)


def roomba(t):
    t.color("green")
    t.width(3)
    t.up()
    t.goto(-home_size / 2, home_size / 2 - 10)
    t.down()

    for i in range(0, (math.ceil(home_size / 40)) - 1):
        t.setheading(0)
        t.forward(20)

        # dx di 20
        t.right(90)
        t.forward(home_size - 20)
        draw_roomba(t)
        # forward_with_roomba(home_size - 20,t)

        t.left(90)
        t.forward(20)

        t.left(90)
        t.forward(home_size - 20)
        draw_roomba(t)


t = turtle.Turtle()
t.speed(0)

draw_room(t)
draw_roomba(t)
roomba(t)

input("Press Enter to continue...")
