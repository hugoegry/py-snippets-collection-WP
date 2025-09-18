"""
📌 This exercise uses the Python turtle module to draw regular polygons.
You are asked to write a function called draw_polygon(sides) that takes one parameter, sides, which is an integer representing the number of sides of the polygon.
"""

import turtle
from turtle import *


def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        forward(100)
        right(angle)
    turtle.exitonclick()


draw_polygon(int(input("Enter number of sides: ")))
