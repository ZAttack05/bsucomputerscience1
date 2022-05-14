import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(250000))
print("popzero", popzero.timeit(number=1000))

#x = list(range(200000))
print("popend", popend.timeit(number=1000))


