"""
File: countfib.py
Prints the the number of calls of a recursive Fibonacci
function with problem sizes that double.
"""

from counter import Counter

c=0

def fib(n):
    global c
    c+=1
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib1(n, counter = None):
    """Count the number of calls of the Fibonacci
    function."""
    if counter: counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)

problemSize = 2
oldcounter=1
print("%12s%15s%10s" % ("Problem Size", "Calls", "Ratio"))
for count in range(33):
    counter = Counter()
    c=0
    # The start of the algorithm
    #fib(problemSize, counter)
    fib(problemSize)
    # The end of the algorithm
    
    #print("%12d%15s%   0.3f" % (problemSize, counter, counter.getValue()/oldcounter))
    print("%12d%15s" % (problemSize, c))
    problemSize += 1
    #oldcounter = counter.getValue()
