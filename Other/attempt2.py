from turtle import Turtle
t = Turtle()

def main():
    htopright, vtopright = firstSquare()
    squarecount = int(input("How many squares do you wish to create?"))
    calculateCords(htopright, vtopright, squarecount)

    

def pickColor():
    from random import random
    r = random()
    g = random()
    b = random()
    return r, g, b

def firstSquare():
    r, g, b = pickColor()
    t.up()
    t.goto(200, 100)
    t.down()
    t.fillcolor(r, g, b)
    t.begin_fill()
    t.goto(200, -100)
    t.goto(-200, -100)
    t.goto(-200, 100)
    t.goto(200, 100)
    t.end_fill()
    vtopright = [400]
    htopright = [200]
    return htopright, vtopright

def calculateCords(htopright, vtopright, squarecount):
    side, direction = directionside()
    if direction == 1:
        """This means that the rectangle will be horizontal"""
        if side == 1:
            """This means the rectangle will be on the top third of the larger rectangle"""
        else:
            """This means the rectangle will be at the bottom third of the larger rectangle"""
    else:
        """This means that the rectangle will be verticle"""
        if side == 1:
            """This means the rectangle will be on the right side of the larger rectangle"""
        else:
            """This means the rectangle will be on the left side of the larger rectangle"""
        


def directionside():
    from random import randint
    side = randint(1, 2)
    direction = randint(1, 2)
    return side, direction

main()