count = 0
def fib(n):
    global count
    count = count + 1
    #print("n=",n, count)
    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(37), count)
