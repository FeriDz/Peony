from turtle import *
from colorsys import *
bgcolor('black')
tracer(5)
pensize(5)
hideturtle()
h = 0
def draw(angle, n):
    circle(-n, 30)
    left(angle)
    circle(n, 120)
for i in range(125):
    c = hsv_to_rgb(h,1,1)
    h += 0.007
    pencolor(c)
    goto(0,0)
    right(30)
    draw(60, i)
    draw(90, i)
    draw(120, i)
    draw(150, i)
    draw(180, i)
done()