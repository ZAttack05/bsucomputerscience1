'''Imports'''
import turtle
import random

'''This function cretes a mountain using recursion.'''
def mountain(l, t,n):
    if l > 38: #Base case
        t.right(n)
        t.forward(l)
        t.right(n + 90)
        t.forward(l)
        t.left(n * 2 + 90)
        mountain(random.randint(30,100), t, random.randint(30,35)) #Recursive call

'''The main function of the program.'''
def main():
    '''This area just gets the turtle in the right spot to draw'''
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.up()
    t.backward(300)
    t.down()
    t.setheading(90)
    '''Mountain call. Uses a slightly random angle, as well as a random length.'''
    mountain(random.randint(30, 100), t, random.randint(30,35))
    myWin.exitonclick()

if __name__ == "__main__":
    main()
