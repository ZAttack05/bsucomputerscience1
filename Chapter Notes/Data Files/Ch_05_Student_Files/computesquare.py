"""
File: computesquare.py
Illustrates the definition of a main function.
"""
import odd1

def main():
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)
    print("5 is odd:", odd1.odd(5), "5 square is", square(5))

def square(x):
    """Returns the square of x. """
    return x * x

# The entry point for program execution
if __name__ == "__main__":
    main()
