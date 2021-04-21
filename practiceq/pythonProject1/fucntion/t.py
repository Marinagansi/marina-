from turtle import *
screen=Screen()
pen=Turtle()
pen.shape("turtle")
pen.color('green')
pen.fillcolor("red")
pen.width(5)
pen.speed(5)
pen.begin_fill()#pen.fillcolor ni rakhn parxa yesma
pen.forward(200)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(100)
pen.end_fill()
for i in range(4):
    pen.right(90)
    pen.forward(200)
pen.penup()
pen.goto(50,50)


done()
