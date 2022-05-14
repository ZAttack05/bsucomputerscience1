"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""
import os
# Take the inputs
fileName = input("Enter the file name: ")
while not os.path.exists(fileName):
    fileName = input("Files does not exist, enter the file name: ")
    
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
wordslist = text.split()
words = len(wordslist)

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"

# Generate double vowels
doubleVowels = []
for v1 in vowels:
    temp = []
    for v2 in vowels:
        doubleVowels.append(v1+v2)


    
for word in wordslist:
    for vowel in vowels:
        syllables += word.count(vowel)
    for dv in doubleVowels:
        syllables -= word.count(dv)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")     


