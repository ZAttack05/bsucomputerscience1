'''
docstring for the module
'''
import computesquare

def odd(num):
    ''' test if num is odd'''
    if num%2 ==1:
        return True
    else:
        return False

def even(num):
    ''' test if num is even'''
    return not odd(num)

def summation(low, high):
    total = 0
    if low > high:
        low, high=high,low
    for num in range(low, high+1):
        total += num
    return total


def main():
    print("5 is even:", even(5), "\n5 square is", computesquare.square(5))
    summ = summation(10,1)
    print("summ =", summ)


# The entry point for program execution
if __name__ == "__main__":
    main()
