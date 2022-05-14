def odd(x):
    """ Returns True if x is odd or False otherwise."""
    if x % 2 == 1:
        return True
    else:
        return False

def even(x):
    return not odd(x)

print(odd(5))
print(even(5))
