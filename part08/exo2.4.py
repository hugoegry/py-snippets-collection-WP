"""
📌 This exercise uses the Python turtle module to draw a spiral pattern.
"""

import turtle
from turtle import *


def drow_spiral(tourns=360):
    colors = ["red", "purple", "blue", "green", "orange", "yellow"]
    t = turtle.Pen()
    turtle.bgcolor("black")
    for x in range(tourns):
        t.pencolor(colors[x % len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
    turtle.exitonclick()


drow_spiral()
