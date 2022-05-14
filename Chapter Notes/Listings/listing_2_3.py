import time

def sumOfN(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

def sumOfN1(n):
    start = time.time()
    theSum = (n*(n+1))/2
    end = time.time()

    return theSum, end-start      

for i in range (50):
   print("Sum is %d required %10.7f seconds"%sumOfN(10000000))
   
