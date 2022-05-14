# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#queue.py

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(23)
q.enqueue(4)
q.enqueue(2435)
q.enqueue(1234)
print(q.isEmpty())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.isEmpty())
