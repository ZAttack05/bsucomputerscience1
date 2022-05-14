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

class LDequeue:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def addRear(self, item):
        current = self.head
        temp = Node(item)
        if current == None:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            while current != None:
                previous = current
                current = current.getNext()
            previous.setNext(temp)

    def addFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def removeFront(self):
        current = self.head
        temp = current
        popped = temp.getData()
        current = current.getNext()
        self.head = current
        return popped

    def removeRear(self):
        current = self.head
        previous = None
        while True:
            if current.getNext() == None:
                break
            else:
                previous = current
                current = current.getNext()
        
        removed = current.getData()

        if previous == None:
            self.head = None
        else:
            previous.setNext(current.getNext())

        return removed
        
            

q = LDequeue()

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