# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#deque.py


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Deque()

q.addFront(34)
q.addFront(4)
q.addRear(9)
print(q.removeFront())
q.addFront(23)
print(q.removeRear())
print(q.removeFront())
print(q.removeRear())
print(q.size())
print(q.isEmpty())