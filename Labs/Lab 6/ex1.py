'''
Name: Zach Nichols
Program: ex1.py
Function: Calculates the probability of at least one pair of people out of n number of people having the same birtdhay but checking 1000 times if any of the group of n people have a match.
'''

'''Imports random for deciding birthdays'''
import random

'''The main function of the program'''
def main():
    '''Initializes variables for a file, n (the number of people), a list of matching birthdays (T/F) and the list of probabilities for each n value.'''
    f = open("Birthday Probability.csv", "w")
    f.write("%s, %s\n" %("Probability %", "Number of People"))
    n = 5

    while n <= 50: #Runs a loop for 5 < n < 50 times
        sum = 0.0
        mblist = []
        for i in range(999): #Runs a loop for 1000 times to get a decent probability
            blist = []
            for k in range(n + 1): #Creates a new birthday for each loop
                v = random.randint(1,366)
                blist.append(v)
            a = compare(blist, n) #Compares the list of birthdays then appends the value receieved to a newer list
            if a == True:
                sum += 1
        
        '''Calculates the probability (in percent).'''
        sum = probability(sum)

        '''Prints the value of n used alongside the probabiltiy of birthdays matching'''
        f.write("%f, %d\n"%(sum, n))
        
        n += 1

    '''Closes the file'''
    f.close()

'''Compares each value of n, the algorithm sorts it from least to greatest to ensure the matches are right next to each other.
    If a match is found, the loop breaks and the function returns "True".'''
def compare(blist, n):
    matchingBirthdays = False
    blist.sort()
    for i in range(n):
        if blist[0] == blist[1]:
            matchingBirthdays = True
            return matchingBirthdays
        blist.pop(0)

    return matchingBirthdays

'''Calculates the probability (in percent).'''
def probability(sum):
    sum = sum / 10
    return sum

if __name__ == "__main__":
    main()





