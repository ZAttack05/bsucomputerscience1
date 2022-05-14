from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString: #Coverts string to a queue
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront() #Grabs and removes the first character
        last = chardeque.removeRear() #Grabs and removes the last character.
        if first == " ": #Checks to make sure the first character is not a space
            first = chardeque.removeFront()
        if last == " ": #Checks to make sure the last character is not a space
                    last = chardeque.removeRear()
        if first != last: #Checks if characters are equal.
            stillEqual = False
            break

    return stillEqual #Returns result.

'''Test cases print out.'''
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("I PREFER PI"))
print(palchecker("BEMIDJI STATE UNIVERSITY"))
print(palchecker("RACECAR RACECAR"))