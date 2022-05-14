def main():
    from turtle import Turtle
    t = Turtle()
    t.up()
    t.speed(300)
    r, g, b = pickColor()
    t.goto(200, 200)
    t.down()
    t.fillcolor(r, g, b)
    t.goto(200, -200)
    t.goto(-200, -200)
    t.goto(-200, 200)
    t.goto(200, 200)
    t.begin_fill()
    sqcount = int(input("How many squares do you desire?"))
    squares = 0
    hdim = [400]
    vdim =[400]
    t.speed(1)
    drawSquare(t, r, g, b, sqcount, hdim, vdim, squares)

def pickColor():
    from random import random
    from random import seed
    seed(1, 256)
    r = random()
    g = random()
    b = random()
    return r, g, b

def drawSquare(t, r, g, b, sqcount, hdim, vdim, squares):
    if sqcount == 0:
        return
    r, g, b = pickColor()
    direction, side = pickDirection()
    sqspot = pickSquare(squares)
    """Check for vertical square"""
    if (direction == 1): 
        verticle = vdim[sqspot]
        horizontal = hdim[sqspot] / 3
        t.up()
        """Check for left or right side square if == 1 then right side"""
        if (side == 1):
            t.goto(hdim[sqspot], vdim[sqspot])
            t.down()
            t.goto(horizontal, verticle)
            t.setheading(180)
            t.forward(verticle)
            t.setheading(270)
            t.forward(horizontal)
            t.setheading(0)
            t.forward(verticle)
            t.setheading(90)
            t.forward(horizontal)
        else:
            y = vdim[sqspot] * -1
            t.goto(y, horizontal)
            t.down()
            t.setheading(180)
            t.forward(verticle)
            t.setheading(90)
            t.forward(horizontal)
            t.setheading(0)
            t.forward(verticle)
            t.setheading(270)
            t.forward(horizontal)

        """Check for horizontal rectangle"""
    else:
        verticle = vdim[sqspot] / 3
        horizontal = hdim[sqspot]
        """Check for up or down square if one then top side"""
        if (side == 1):
            t.goto(hdim[sqspot], vdim[sqspot])
        else:
            y = hdim[sqspot] * -1
            t.goto(horizontal, y)
    
        




    squares += 1
    
def pickSquare(squares):
    from random import random
    from random import seed
    seed(1, squares)
    sqspot = random()
    sqspot = round(sqspot)
    return sqspot

def pickDirection():
    from random import random
    from random import seed
    seed(1, 2)
    direction = random()
    side = random()
    direction = round(direction)
    side = round(side)
    return direction, side

main()