class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LStack:
    def __init__(self):
        self.head = None

    def push(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def peek(self):
        return self.head.getData()

    def isEmpty(self):
        return self.head == None

    def pop(self):
        current = self.head
        current = current.getNext()
        self.head = current
    
linkedStack = LStack()
linkedStack.push(1)
linkedStack.push(6435)  
linkedStack.push(35)  
linkedStack.push(4)
linkedStack.push(3534)

print(linkedStack.size())
print(linkedStack.peek())
linkedStack.pop()
print(linkedStack.isEmpty())

print(linkedStack.size())
print(linkedStack.peek())
linkedStack.pop()
print(linkedStack.isEmpty())

print(linkedStack.size())
print(linkedStack.peek())
linkedStack.pop()
print(linkedStack.isEmpty())

print(linkedStack.size())
print(linkedStack.peek())
linkedStack.pop()
print(linkedStack.isEmpty())

print(linkedStack.size())
print(linkedStack.peek())
linkedStack.pop()
print(linkedStack.isEmpty())

    

