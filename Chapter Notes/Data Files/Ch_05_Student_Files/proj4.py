"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")

adjectives = ("RED", "SORE", "GREEN", "YELLOW", "BIG", "SMALL")

def sentence():
    """Builds and returns a sentence."""
    probability = random.randint(1, 2)
    if probability == 1:
        return nounPhrase() + " " + verbPhrase() + "."
    else:
        return nounPhrase() + " " + verbPhrase() + " and " + \
        nounPhrase() + " " + verbPhrase() + "."

def nounPhrase():
    """Builds and returns a noun phrase."""
    probability = random.randint(1, 2)
    if probability == 1:
        return random.choice(articles) + " " + random.choice(nouns)
    else:
        return random.choice(articles) + " " +random.choice(adjectives) +\
        " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    probability = random.randint(1, 2)
    if probability == 1:
        return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()
    else:
        return random.choice(verbs) + " " + nounPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()







'''
def nounPhrase():
    '''
'''Returns a noun phrase, which is an article followed
    by a noun, and an optional prepositional phrase.'''
'''
    phrase = random.choice(articles) + ' ' + random.choice(nouns)
    prob = random.randint(1, 4)
    if prob == 1:
        return phrase + ' ' + prepositionalPhrase()
    else:
        return phrase
'''
