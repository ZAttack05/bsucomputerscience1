'''This function draws a "countryside church building minus the cross.", or as I like to call it, a crude picture of a house.'''

import turtle
t = turtle.Turtle()
t.up()
t.shape("turtle")

'''Main function of the program. Gathers input and then calls drawHouse()'''
def main():
    scale = (input("Please enter the scale size between 0 and 5. Press enter for default value. "))
    if scale == "" or scale == "/n":
        scale = 1.0
    else:
        scale = float(scale)
    if scale > 5:
        print("Scale size needs to be between 0 and 5.")
        main()
    blc = float(input("Please enter an x coordinate. ")), float(input("Please enter a y coordinate. "))
    drawHouse(blc, scale)
    turtle.done()

'''Handles all of the functions required to draw the house'''
def drawHouse(blc, scale):
    distance = 100 * scale
    t.goto(blc)
    drawSquare(distance)
    drawRoof(distance)
    t.goto(blc)
    drawWindow(distance)
    t.goto(blc)
    drawDoor(distance)
    t.goto(blc)

'''Draws a square'''
def drawSquare(distance):
    t.setheading(0)
    t.down()
    for i in range(4):
        t.forward(distance)
        t.left(90)
    t.up()

'''Draws the roof of the house'''
def drawRoof(distance):
    t.up()
    t.setheading(90)
    t.forward(distance)
    t.setheading(60)
    t.down()
    for i in range(3):
        t.forward(distance)
        t.right(120)
    t.setheading(0)
    t.up()

'''Draws a window. Filled in 4 major quadrants to replicate the Microsoft Windows logo as a fun gag'''
def drawWindow(distance):
    windis = distance / 6
    t.setheading(0)
    t.up()
    t.forward(windis)
    t.left(90)
    t.forward(windis)
    windis = windis / 2
    t.fillcolor("blue")
    t.begin_fill()
    drawSquare(windis)
    t.end_fill()
    t.setheading(90)
    t.forward(windis)
    t.fillcolor("red")
    t.begin_fill()
    drawSquare(windis)
    t.end_fill()
    t.forward(windis)
    t.fillcolor("green")
    t.begin_fill()
    drawSquare(windis)
    t.end_fill()
    t.setheading(270)
    t.forward(windis)
    t.fillcolor("yellow")
    t.begin_fill()
    drawSquare(windis)
    t.end_fill()
    t.up()

'''Draws the door and a handle and a circular knov'''
def drawDoor(distance):
    t.setheading(0)
    t.forward(distance * 7/8)
    t.setheading(90)
    t.down()
    for i in range(2):
        t.forward(distance/2)
        t.left(90)
        t.forward(distance/4)
        t.left(90)
    t.up()
    t.setheading(90)
    t.forward(distance/4)
    t.left(90)
    t.forward(distance/20)
    t.down()
    t.circle(distance / 30)
    t.up()

if __name__ == "__main__":
    main()