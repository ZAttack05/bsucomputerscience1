import turtle
import random

def main():
    t = turtle.Turtle()
    x1 = -100
    y1 = 0
    x2 = 200
    y2 = 0
    iterations = 2
    m(x1, y1, x2, y2, t, iterations)
    turtle.done()

def m(x1, y1, x2, y2, t, it):
    if it == 0:
        t.up()
        t.goto(x1,y1)
        t.down()
        t.goto(x2, y2)
    else:
        midx = (x1+x2)//2
        midy = (y1+y2)//2 + random.randint(0,50)
        m(x1, y1, midx, midy, t, it-1)
        m(midx, midy, x2, y2, t, it-1)
        
main()