def runForever(n):
    if n > 0:
        runForever(n-1)
    else:
        #runForever(n-1)
        return

runForever(10)
