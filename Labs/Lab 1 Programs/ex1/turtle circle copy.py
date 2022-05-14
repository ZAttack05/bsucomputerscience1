'''This program replicates turtle's .cirlce method to draw a circle'''
import turtle
t = turtle.Turtle()
import math

'''Draws a circle replicating turtle's .cirlce() method.'''
def drawCircle(radius):

    t.down()
    distance = 2 * math.pi * radius / 120
    for count in range(120):
        t.forward(distance)
        t.left(3)
    return distance

'''Main function of the program'''
def main():
    t.home
    radius = int(input("Enter radius: "))
    t.speed(1)
    drawCircle(radius)
    turtle.done()

if __name__ == "__main__":
    main()