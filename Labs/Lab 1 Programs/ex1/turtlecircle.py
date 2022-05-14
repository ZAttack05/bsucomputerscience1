'''This program uses turtle's .circle method to draw a circle'''
import turtle
t = turtle.Turtle()

def main():
    t.home
    radius = int(input("Enter radius: "))
    t.speed(1)
    t.circle(radius)
    turtle.done()

if __name__ == "__main__":
    main()