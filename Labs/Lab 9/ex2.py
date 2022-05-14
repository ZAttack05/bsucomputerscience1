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

class LQueue:
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

    def dequeue(self):
        current = self.head
        temp = current
        popped = temp.getData()
        current = current.getNext()
        self.head = current
        return popped
    
    def enqueue(self,item):
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
        
            
q = LQueue()
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

