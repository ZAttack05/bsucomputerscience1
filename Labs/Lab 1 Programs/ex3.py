'''This program draws a Christmas tree with ornaments'''

import turtle
import random
t = turtle.Turtle()
t.up()
t.shape("turtle")
t.speed(300)

'''Main function of the program'''
def main():
    scale = (input("Please enter the scale size. Press enter for default value. "))
    if scale == "" or scale == "/n":
        scale = 1.0
    else:
        scale = float(scale)
    blc = float(input("Please enter an x coordinate. ")), float(input("Please enter a y coordinate. "))
    drawTree(scale, blc)
    t.goto(blc)
    drawTrunk(scale)
    turtle.done()

'''Handles the fucntions required to draw the tree'''
def drawTree(scale, blc):
    t.up()
    t.goto(blc)
    distance = scale * 300
    drawTriangle(distance)
    drawOrn(blc, distance)
    for i in range(2):
        t.left(60)
        t.forward(distance)
        distance /= 2
        t.setheading(270)
        t.forward(distance / 2)
        t.setheading(180)
        t.forward(distance / 2)
        drawTriangle(distance)
        blc = t.position()
        drawOrn(blc, distance)

'''Draws the general 3 triangles required to make up the tree'''
def drawTriangle(distance):
    t.setheading(0)
    t.down()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(3):
        t.forward(distance)
        t.left(120)
    t.end_fill()
    t.up()

'''Draws ornaments in a pattern with random colors'''
def drawOrn(blc, distance):
    t.goto(blc)
    t.setheading(30)
    t.forward(distance * 0.2)
    t.setheading(0)
    t.up()
    for i in range(3):
        drawCircleSet(distance)
        t.left(120)
    t.goto(blc)
    t.setheading(0)

'''Used by drawOrn() to draw a "set" of cirlces. Just makes it easier to draw a set of ornaments per triangle'''
def drawCircleSet(distance):
    for i in range(2):
        color = pickColor()
        t.forward(distance / 3)
        t.down()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(distance * .04)
        t.end_fill()
        t.up()
        
'''Picks a random color'''
def pickColor():
    num = random.randint(1, 3)
    if num == 1:
        color = "blue"
    elif num == 2:
        color = "red"
    elif num == 3:
        color = "yellow"
    return color

'''Draws the tree trunk'''
def drawTrunk(scale):
    t.fillcolor("brown")
    t.up()
    t.forward(scale * 300 * 1/3)
    distance = scale * 100
    t.down()
    t.begin_fill()
    t.setheading(0)
    for i in range(2):
        t.forward(distance)
        t.right(90)
        t.forward(distance * 0.8)
        t.right(90)
    t.end_fill()
    t.up()

if __name__ == "__main__":
    main()