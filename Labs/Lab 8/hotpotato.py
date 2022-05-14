'''imports'''
from pythonds.basic.queue import Queue
import random

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

'''Creates a random number, the passes it along to play hot potatoe!'''
def main():
    num = random.randint(0, 1000) #Chooses a random number between 0, and 1000 to play the game for. Reasonably, you probably don't want to play for more than 1000 iterations, but my computer will.
    print(str(num)) #Prints the iterations, in case you wanted to test and make sure it was correct in terms of interations.
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], num))

if(__name__ == "__main__"):
    main()
