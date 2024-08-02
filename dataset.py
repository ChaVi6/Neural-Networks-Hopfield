from turtle import *
import random
from PIL import Image

d = {2: 'circle', 3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon'}

#Генерация датасета

def generate(tur1, a, b, c1, c2):
    if a != 2:
        for n in range(a):
            tur1.forward(c1)
            tur1.left(360.0 / a)
    else:
        tur1.circle(c1)

    tur1.penup()
    tur1.goto(-(c1 + 10), -(c1 + 10))
    tur1.pendown()

    if b != 2:
        for j in range(b):
            tur1.forward(c1)
            tur1.left(360.0 / b)
    else:
        tur1.circle(c2)

for i in range(0, 5):
    a1 = random.randint(2, 7)
    b1 = a1
    while b1 == a1:
        b1 = random.randint(2, 7)
    c1 = random.randint(25, 35)
    c2 = random.randint(25, 35)
    tur2 = Turtle()
    tur2.pencolor('black')  # устанавливаем цвет контура
    tur2.fillcolor('white')  # устанавливаем цвет заливки
    tur2.speed(0)
    tur2.hideturtle()
    screen1 = Screen()
    screen1.setup(200, 200)
    if (i % 3) == 0:
        screen1.bgpic('C:/Hopfield/b1.png')
    if (i % 3) == 1:
        screen1.bgpic('C:/Hopfield/b2.png')
    if (i % 3) == 2:
        screen1.bgpic('C:/Hopfield/b3.png')

    tur2.begin_fill()
    generate(tur2, a1, b1, c1, c2)
    tur2.end_fill()

    screen = tur2.getscreen()
    canvas = screen.getcanvas()
    filename = str(i) + "_" + d[a1] + "_" + d[b1]
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save("C:/Hopfield/train/" + filename + ".png")

    tur2.clear()
