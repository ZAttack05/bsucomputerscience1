'''Draws a mystical, winter scene...'''
import turtle
import math
import random
t = turtle.Turtle()
t.up()

'''Main function of program, gathers input before passing to winterScene()'''
def main():
    turtle.tracer(False)
    scale = input("Enter a scale or press enter for default value: ")
    if scale == "" or scale == "/n":
        scale = 1.0
    else:
        scale = float(scale)
    blc = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
    winterScene(blc, scale)
    turtle.done()

def winterScene(blc, scale):
    housescale = scale * 2
    drawHouse(blc, housescale)
    t.up()
    t.goto(blc)
    t.setheading(0)
    t.forward(300 * scale)
    blc = t.position()
    smscale = scale * 1/2
    drawSnowman(smscale, blc)
    t.up()
    t.goto(blc)
    t.setheading(0)
    t.forward(80 * scale)
    t.left(90)
    t.forward(50 * scale)
    blc = t.position()
    tscale = scale * 0.8
    t.width(1)
    t.pencolor("black")
    drawTree(tscale, blc)
    t.goto(blc)
    drawTrunk(tscale)
    print("Walking in a winter wonderland...")

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

    '''Handles the functions for drawing the snowman'''
def drawSnowman(scale, blc):
    t.up()
    t.goto(blc)
    radius = drawBody(scale)
    drawFace(scale)
    t.up()
    t.goto(blc)
    drawHat(scale, radius)
    t.up()
    t.goto(blc)
    t.setheading(90)
    t.forward(radius * 2 * 3/4)
    blc = t.position()
    drawArms(scale, blc, radius)


'''Draws the body using a for loop'''
def drawBody(scale):
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
def drawFace(scale):
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
def drawArms(scale, blc, radius):
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

'''Draws a lil hat for him'''
def drawHat(scale, radius):
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