from profiler import Profiler
from algorithms import insertionSort

p = Profiler()
p.test(insertionSort, size = 105, comp = True,
       exch = True, trace = False)
