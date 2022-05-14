'''This program draws a circle'''
import turtle
import math

'''Draws circle'''
def drawCircle(t, radius, xPosition, yPosition):
    t.speed(10)
    t.up()
    t.goto(xPosition, yPosition)
    t.right(180)
    t.forward(radius)
    t.right(90)
    t.down()
    distance = 2 * math.pi * radius / 120
    for count in range(120):
        t.forward(distance)
        t.right(3)
    return distance

'''Main function of the program'''
def main():
    t = turtle.Turtle()
    t.home
    xPosition = int(input("Enter X position: "))
    yPosition = int(input("Enter Y position: "))
    radius = int(input("Enter radius: "))
    distance = drawCircle(t, radius, xPosition, yPosition)
    distanceTravelled = (distance * 120) + radius
    print("The turtle travelled " + str((distanceTravelled)) + " pixels.")
    turtle.done()

if __name__ == "__main__":
    main()