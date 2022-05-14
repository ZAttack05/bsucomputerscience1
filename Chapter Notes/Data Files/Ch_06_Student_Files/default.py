def repToInt(repString, base = 2):
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent = exponent - 1
    return decimal


def example(required, option1 = 2, option2 = 3):
   print(required, option1, option2)

'''
print(repToInt('1001', 8))
print(repToInt('1001'))
example(1, 10)
example(1, option2=20, option1=10)
'''
replacements = {"I":"you", "me":"you", "my":"your", "am":"are",
                "we":"you", "us":"you", "mine":"yours"}

def changePerson(sentence):
    '''Replaces first person pronouns with second person pronouns.'''
    def getWord(word):
        return replacements.get(word, word)
    return ' '.join(map(getWord, sentence.split()))
    
print(changePerson("I you mine fine"))
