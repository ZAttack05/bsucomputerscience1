from functools import reduce

def subs(x,y):
    print("x=",x, "y=",y)
    return x-y

def adds(x,y):
    print("x=",x, "y=",y)
    return x+y


#def odd(n): return n%2==1

#print(list(filter(odd, range(10))))


data=[1,2,3,4]
print(reduce(adds, data))
'''
x, y
1, 2
-1, 3
-4, 4

-8 is the result.
'''
