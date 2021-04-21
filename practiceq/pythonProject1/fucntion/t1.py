import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
def drawCircle(x,y,r):
    pen.pu()
    pen.goto(x,y-r)
    pen.pd()
    pen.circle(r)
for i in range(20,200,20):
    drawCircle(0,0,i)
def makepicture(x,y,r):
    if r<10:
        drawCircle(x,y,r)
    else:
        drawCircle(x,y,r)
        makepicture(x+r,y,r/2)
makepicture(200)
turtle.done()