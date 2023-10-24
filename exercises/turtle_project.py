"""Turtle project! Wave of Kanagawa!"""

__author__ = "730658911"

from turtle import Turtle, colormode, done 
import turtle

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    turtle.speed("fastest")
    turtle.tracer(0, 0)
    window = turtle.Screen()
    window.setup(700, 700)
    window.bgcolor(248, 236, 121)
    window.title("clashing waves")
    background_wave(wave, -400, 50)
    second_wave(wave, -250, 100)
    third_wave(wave, 360, -200)
    sun(wave, -30, -45)
    cloud(wave, 100, 170, 6)
    cloud(wave, 250, 80, 4)
    cloud(wave, -250, 200, 4)
    turtle.hideturtle()
    turtle.update()
    done()


wave: Turtle = Turtle()


def background_wave(bwave: Turtle, x: float, y: float) -> None:
    """This creates the biggest wave in the scene, furthest from the viewer at x, y."""
    bwave.pensize(1)
    bwave.pencolor("blue")
    bwave.fillcolor(16, 32, 122)
    bwave.penup()
    bwave.goto(x, y)
    bwave.left(50)
    bwave.pendown()
    bwave.begin_fill()
    bwave.forward(200)
    i: int = 0
    while (i < 6):
        bwave.right(15)
        bwave.forward(50)
        i += 1

    bwave.right(120) 

    z: int = 0
    while (z < 13):
        wave_angle: float = 15
        bwave.forward(50)
        bwave.left(wave_angle)
        wave_angle = wave_angle * 1.5
        z += 1

    bwave.forward(280)
    bwave.right(125)
    bwave.forward(500)
    bwave.right(90)
    bwave.forward(750)
    bwave.right(90)
    bwave.forward(600)
    bwave.end_fill()


def second_wave(swave: Turtle, x: float, y: float) -> None:
    """This creates the second wave in our scene, a little closer to the viewer than the first wave at x, y."""
    swave.fillcolor(75, 147, 224)
    swave.pencolor(75, 147, 224)
    swave.penup()
    swave.goto(x, y)
    swave.right(50)
    swave.pendown()
    swave.forward(20)

    swave.begin_fill()
    i: int = 0
    while (i < 6):
        swave.right(15)
        swave.forward(50)
        i += 1

    swave.right(120) 

    z: int = 0
    while (z < 13):
        wave_angle: float = 15
        swave.forward(50)
        swave.left(wave_angle)
        wave_angle = wave_angle * 0.98
        z += 1

    swave.forward(300)
    swave.right(125)
    swave.forward(350)
    swave.right(90)
    swave.forward(758)
    swave.right(90)
    swave.forward(415)
    swave.end_fill()


def third_wave(twave: Turtle, x: float, y: float) -> None:
    """This creates our smallest wave, closest to the viewer at x, y."""
    twave.fillcolor(176, 221, 244)
    twave.pencolor(176, 221, 244)
    twave.penup()
    twave.goto(x, y)
    twave.pendown()
    twave.begin_fill()
    twave.left(45)
    twave.forward(10)
    i: int = 0
    wave_angle: float = 5
    while (i < 9):
        twave.left(wave_angle)
        twave.forward(20)
        wave_angle = wave_angle * 1.3
        i += 1
    twave.left(120)
    z: int = 0
    while (z < 14):
        wave_angle2: float = 15
        twave.forward(8)
        twave.right(wave_angle2)
        wave_angle2 = wave_angle2 * 1.2
        z += 1
    if z >= 14:
        while (z < 20):
            wave_angle3: float = 1
            twave.left(wave_angle3)
            twave.forward(50)
            z += 1
    twave.forward(100)
    twave.left(160)
    twave.forward(480)
    twave.left(90)
    twave.forward(200)
    twave.end_fill()


def planet(cc: Turtle) -> None:
    """This creates a circle shape."""
    cc.setheading(90)
    i: int = 0
    while (i < 40):
        cc.right(15)
        cc.forward(17)
        i += 1


def sun(sun: Turtle, x: float, y: float) -> None:
    """This creates the sun in our scene at x, y, implementing the planet function."""
    sun.pencolor("red")
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.fillcolor("red")
    sun.begin_fill()
    planet(wave)
    sun.end_fill()
    sun.penup()


def curve(cv: Turtle, z: float) -> None:
    """This creates a curve with size z."""
    i: int = 0
    wave_angle: int = 10
    while (i < 10):
        cv.right(wave_angle)
        cv.forward(z)
        i += 1


def cloud(cl: Turtle, x: float, y: float, z: float) -> None:
    """This creates a cloud with size z in our scene at x, y, implementing the curve function."""
    cl.pensize(2)
    cl.pencolor("white")
    cl.fillcolor("white")
    cl.penup()
    cl.goto(x, y)
    turtle.setheading(90)
    cl.pendown()
    cl.right(40)
    curve(wave, z)
    cl.begin_fill()
    cloud_angle: float = 60
    for i in range(7):
        cl.left(cloud_angle)
        curve(wave, z)
        cloud_angle = cloud_angle * 0.98
    cl.left(80)
    curve(wave, z)
    cl.end_fill()


if __name__ == "__main__":
    main()