"""
📌 This exercise asks you to use the Python turtle module to reproduce one or more provided images using as few lines of code as possible.
"""

import turtle, random
from turtle import *
from math import *


def gotoPose(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# 1 rosace
def form1(t, radius=100, repetitions=36, color="purple"):
    t.color(color)
    t.width(2)
    for _ in range(repetitions):
        t.circle(radius)
        t.left(360 / repetitions)


# 2 Spirale de carre
def form2(t, size=200, steps=36):
    colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow"]
    for i in range(steps):
        t.color(random.choice(colors))
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.right(10)
        size -= 5


# 3 Flocon
def form3(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        form3(t, order - 1, size)
        t.left(60)
        form3(t, order - 1, size)
        t.right(120)
        form3(t, order - 1, size)
        t.left(60)
        form3(t, order - 1, size)


def draw_koch_snowflake(t, order=3, size=300):
    for _ in range(3):
        form3(t, order, size)
        t.right(120)


# 4
def form4(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        form4(t, order - 1, size / 2)
        t.forward(size / 2)
        form4(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        form4(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)


def main():
    screen = turtle.Screen()
    screen.setup(1200, 800)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(10000)
    t.hideturtle()

    # Rosace
    gotoPose(t, -400, 200)
    form1(t)

    # Spirale carre
    gotoPose(t, 200, 200)
    form2(t)

    # Flocon
    gotoPose(t, -350, -100)
    draw_koch_snowflake(t, 3, 200)

    # triangle
    gotoPose(t, 150, -150)
    form4(t, 4, 250)

    screen.exitonclick()


main()
