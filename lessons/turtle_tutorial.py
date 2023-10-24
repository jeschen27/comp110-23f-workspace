"""Turtle art project!"""
__author__ = "730658911"
from turtle import Turtle, colormode, done
colormode(255)
bob: Turtle = Turtle()

bob.penup()
bob.goto(-160,0)
bob.pendown()

bob.fillcolor("pink")
bob.speed(50)

bob.begin_fill()
side_length: int = 300
i = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1
bob.end_fill()

bob.pencolor("black")
bob.pendown()
while (i < 300):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(123)
    i += 1
done()
