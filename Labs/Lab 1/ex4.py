'''This program draws a snowman'''
import turtle
import math
import random

'''Main function of program. Gathers input and then calls drawSnowman()'''
def main():
    t = turtle.Turtle()
    turtle.tracer(False)
    scale = input("Enter a scale or press enter for default value: ")
    if scale == "" or scale == "/n":
        scale = 1.0
    else:
        scale = float(scale)
    blc = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
    drawSnowman(t, scale, blc)
    turtle.done()

'''Handles the functions for drawing the snowman'''
def drawSnowman(t, scale, blc):
    t.up()
    t.goto(blc)
    radius = drawBody(t, scale)
    drawFace(t, scale)
    t.up()
    t.goto(blc)
    drawHat(t, scale, radius)
    t.up()
    t.goto(blc)
    t.setheading(90)
    t.forward(radius * 2 * 3/4)
    blc = t.position()
    drawArms(t, scale, blc, radius)


'''Draws the body using a for loop'''
def drawBody(t, scale):
    radius = 40 * scale
    t.fillcolor("white")
    for i in range(3):
        t.begin_fill()
        t.down()
        t.circle(radius)
        t.end_fill()
        t.up()
        t.setheading(90)
        t.forward(radius * 2 * 3/4)
        t.setheading(0)
    t.up()
    t.right(90)
    t.forward(radius * 2 * 3/4)
    return radius

'''Draws the face. I seperated it out a bit (not into fucntions, to avoid having a lot of them) into seperate sections for the different parts of the face. Those sections will be annotated accordingly'''
def drawFace(t, scale):
    '''Draws the smile'''
    t.up()
    t.setheading(90)
    t.forward(15 * scale)
    smilepos = t.position()
    t.fillcolor("black")
    for i in range (3):
        t.setheading(0)
        t.down()
        t.begin_fill()
        t.circle(5 * scale )
        t.end_fill()
        t.up()
        if i == 0:
            t.left(20)
        else:
            t.left(20 * i)
        t.forward(13 * scale)
    
    t.goto(smilepos)
    t.setheading(180)
    t.right(40)
    t.forward(16 * scale)

    for i in range (2):
        t.setheading(180)
        t.down()
        t.begin_fill()
        t.circle(5 * scale )
        t.end_fill()
        t.up()
        if i == 0:
            t.right(30)
        else:
            t.right(40)
        t.forward(13 * scale)

    '''Draws the nose'''
    t.up()
    t.goto(smilepos)
    t.setheading(90)
    t.forward(20 * scale)
    t.setheading(0)
    t.left(15)
    base = 10 * scale
    height = 30 * scale
    sidelen = math.sqrt(12 ** 2 / 4 + height ** 2)
    t.down()
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(sidelen)
    t.left(150)
    t.forward(sidelen)
    t.left(105)
    t.forward(base)
    t.end_fill()

    '''Draws the eyes'''
    t.fillcolor("black")
    t.up()
    t.goto(smilepos)
    t.setheading(90)
    t.forward(50 * scale)
    smilepos = t.position()
    t.left(90)
    t.forward(15 * scale)
    t.down()
    t.begin_fill()
    t.circle(8 * scale)
    t.end_fill()
    t.up()
    t.goto(smilepos)
    t.setheading(0)
    t.forward(15 * scale)
    t.begin_fill()
    t.down()
    t.setheading(180)
    t.circle(8 * scale)
    t.end_fill()
    t.up

'''Draws the arms, with the fingers being at random angles'''
def drawArms(t, scale, blc, radius):
    t.width(5 * scale)
    t.pencolor("brown")
    t.setheading(90)
    t.up()
    t.forward(radius)
    t.right(90)
    t.forward(radius)
    t.left(30)
    t.down()
    arm = 40 * scale
    t.forward(arm * 7/8)
    hand = t.position()
    t.forward(arm * 1/8)
    t.up()
    t.goto(hand)
    t.down()
    t.setheading(30)
    angle = random.randint(50, 150)
    t.left(angle)
    t.forward(arm * 1/8)
    t.up()
    t.goto(hand)
    t.setheading(30)
    angle = random.randint(50, 150)
    t.right(angle)
    t.down()
    t.forward(arm * 1/8)
    t.up()
    t.goto(blc)
    t.setheading(90)
    t.forward(radius)
    t.left(90)
    t.forward(radius)
    t.setheading(150)
    t.down()
    t.forward(arm * 7/8)
    hand = t.position()
    t.forward(arm * 1/8)
    t.up()
    t.goto(hand)
    t.setheading(150)
    angle = random.randint(50, 150)
    t.left(angle)
    t.down()
    t.forward(arm * 1/8)
    t.up()
    t.goto(hand)
    t.setheading(150)
    angle = random.randint(50, 150)
    t.down()
    t.right(angle)
    t.forward(arm * 1/8)
    t.up()
    t.goto(blc)
    t.hideturtle()

'''Draws a lil hat for him'''
def drawHat(t, scale, radius):
    t.setheading(90)
    for i in range(2):
        t.forward(radius * 2 * 3/4)
    t.forward(radius * 2)
    t.setheading(0)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(15 * scale)
    t.left(90)
    t.forward(5 * scale)
    t.left(90)
    t.forward(10 * scale)
    t.right(90)
    t.forward(20 * scale)
    t.left(90)
    t.forward(12 * scale)
    t.left(90)
    t.forward(20 * scale)
    t.right(90)
    t.forward(10 * scale)
    t.left(90)
    t.forward(5 * scale)
    t.left(90)
    t.forward(15 * scale)
    t.end_fill()
    t.up()

if __name__ == "__main__":
    main()