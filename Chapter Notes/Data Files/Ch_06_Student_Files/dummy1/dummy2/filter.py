from functools import reduce
def odd(n):return n % 2 == 1
#print(list(filter(odd, range(10))))

def subs(x,y): return x-y
data=[1,2,3,4]
print(reduce(subs, data))
