import turtle
from turtle import *
begin_fill()
color('green')
bgcolor('black')
hideturtle()

pensize(10)
turtle.speed('fastest')

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

penup()
left(180)
forward(20)
right(90)
forward(30)
pendown()
begin_fill()
color('black')
forward(140)
left(90)
forward(170-10)
left(90)
forward(150-10)
left(90)
forward(170-10)
penup()
penup()
end_fill()

left(180)
forward(170-10)
right(90)
forward(20)
right(90)
forward(100)
left(90)
forward(50)

pendown()

color('white')

turtle.write('PC', align="center", font="consolas, 70")

penup()

left(180)
forward(10)

pendown()
forward(50)

done()
