'''This is the fibonocci number generator.'''
def fib(n, o, x, number):
    if x == number: #Base case
        return n
    elif x % 2 != 0:
        '''We found we need to have this these if statements to update each number.'''
        return fib(n+o, o, x+1, number) #Recursive call
    else:
        return fib(n, n + o, x + 1, number) #Recursive call

'''Main function of the program.'''
def main():
    number = int(input("Enter a number: "))
    print(fib(0,1,0, number))

if __name__ == '__main__':
    main()
