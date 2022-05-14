"""
File: randomwalk.py

A turtle takes a random walk.
"""

from turtle import Turtle
import random

def randomWalk(t, turns, distance = 20):
    for count in range(turns):
        degrees = random.randint(0, 360)
        if count % 2 == 0:
            t.left(degrees)
        else:
            t.right(degrees)
        distance = random.randint(5,25)
        t.forward(distance)

def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 50, 25)

if __name__ == "__main__":
    main()
