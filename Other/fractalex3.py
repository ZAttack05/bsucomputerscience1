def drawFractalLine(t, length, level):
    if (level == 0):
            t.forward(length)
            return
    length /= 3
    drawFractalLine(t, length, level-1)
    t.left(60)
    drawFractalLine(t, length, level-1)
    t.right(120)
    drawFractalLine(t, length, level-1)
    t.left(60)
    drawFractalLine(t, length, level-1)
def main():
    from turtle import Turtle
    t = Turtle()
    t.home
    t.speed(1000)
    t.down()
    length = int(input("Enter default length"))
    level = int(input("Enter level"))
    for i in range(3):  
        drawFractalLine(t, length, level)
        t.right(120)
        i += 1
main()
    
