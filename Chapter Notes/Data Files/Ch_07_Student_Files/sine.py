'''
B Tian
Trig functions drawn with Turtle
'''

from turtle import Turtle
import math

def drawSine(t):

    for angle in range(1, 360):
        t.goto(angle, 200*math.sin(angle/180*math.pi))
    
def main():
    t = Turtle()
    drawSine(t)

if __name__ == "__main__":
    main()
