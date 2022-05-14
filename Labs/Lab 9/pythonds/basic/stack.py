# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

mystack = Stack()

mystack.push(1)
mystack.push(6435)
mystack.push(35)
mystack.push(4)
mystack.push(3534)
print(mystack.peek())
print(mystack.size())
mystack.pop()
print(mystack.peek())