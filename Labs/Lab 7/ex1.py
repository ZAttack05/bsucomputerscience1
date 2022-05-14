from stack import Stack

'''Does the conversion bit'''
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]


    return newString

'''Main function of the program'''
def main():
    numlist = [15, 30, 267, 32344]

    for i in range(len((numlist))): #To save my time and energy, and just made the test for each number to be a list tested for each item in the list for the base needed.
        print("Number: " + str(numlist[i]))
        print("Number in base three is " + baseConverter(numlist[i], 3))
        print("Number in base seven is " + baseConverter(numlist[i], 7))
        print("Number in base sixteen is " + baseConverter(numlist[i], 16))

if __name__ == "__main__":
    main()

