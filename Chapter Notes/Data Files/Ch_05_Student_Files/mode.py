"""
File: mode.py
Prints the mode of a set of numbers in a file.
"""
def readFile(fileName):
    f = open(fileName, 'r')
    
# Input the text, convert its to words to uppercase, and
# add the words to a list
    words = []
    for line in f:
        wordsInLine = line.split()
        for word in wordsInLine:
            words.append(word.upper())
            
    return words

def mode(words):
# Obtain the set of unique words and their
# frequencies, saving these associations in
# a dictionary
    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number == None:
        # word entered for the first time
            theDictionary[word] = 1
        else:
        # word already seen, increment its number
            theDictionary[word] = number + 1

    print(theDictionary)
# Find the mode by obtaining the maximum value
# in the dictionary and determining its key
    theMaximum = max(theDictionary.values())
    
    maxkey = 0
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            maxkey = key
            break

    return maxkey, theMaximum

def output(key, theMaximum):
    print("The mode is", key, " It occurred ", theMaximum, " times.")
    
def main():
    fName = input("Enter the file name: ")
    li=readFile(fName)
    mod,maxi = mode(li)
    output(mod, maxi)
    
if __name__ == "__main__":
    main()
