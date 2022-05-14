"""
File: min.py
"""

def ourMin(lyst, trace = False):
    """Returns the position of the minimum item."""
    minpos = 0
    current = 1
    while current < len(lyst):
        if trace: print("             ", current,lyst[current], minpos, lyst[minpos])
        if lyst[current] <= lyst[minpos]:
            minpos = current
            if trace: print("smaller found", current, lyst[current], minpos, lyst[minpos])
            #minpos = current
        current += 1
    return minpos

l=[3,7,2,4,5,2,5,1,7,8,1,10,3]
print(ourMin(l, True))
