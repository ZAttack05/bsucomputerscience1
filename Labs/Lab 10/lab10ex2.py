import turtle
import random

def tree(branchLen,t,w, n):
    if branchLen > 5:
        '''We added this if statement to check if the branch length is less than a certain amount, so we can change the color.'''
        if branchLen > 40: #Base case
            t.color("brown")

        else: 
            t.color("green")
        '''We need the turtle to go down here, as later we tell it to go up to avoid going back with the wrong color later'''
        t.down()
        t.width(w)
        t.forward(branchLen) 
        t.right(n)
        tree(branchLen-random.randint(10,15),t, w-3,random.randint(15,25)) #Recursive call
        t.left(n * 2)
        tree(branchLen-random.randint(10,15),t, w-3,random.randint(15,25)) #Recursive call
        t.right(n)
        '''We need this up command here, as to avoid creating issues with the line going backwards and drawing the wrong color.'''
        t.up()
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    '''We added a variable called w for width. We will use this for adjusting the width as the tree is created.'''
    w = 20
    t.color("brown")
    tree(75,t,w, random.randint(15,25))
    myWin.exitonclick()

if __name__ == '__main__':
    main()
