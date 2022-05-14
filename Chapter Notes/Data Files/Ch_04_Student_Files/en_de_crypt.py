
def decryption(sample, distance):
    """This reads sample.txt and uses a for loop to replace each
    character by reading the character's value and subtracting that by one
    to give us the character next to it. Each encrypted character is put
    into the new string and printed after it is done."""
    #f = open("sample.txt",'r')
    #sample = f.read()
    #distance = 1
    plainText = ""
    for ch in sample:
        ordvalue = ord(ch)
        if ord('a') <= ordvalue <= ord('z'):
            cipherValue = ordvalue - distance
            if cipherValue < ord('a'):
                cipherValue = ord('z') - (distance - (ordvalue - ord('a')) - 1)
            plainText += chr(cipherValue)
        else:
            plainText += ch
    return plainText

def encryption(sample, distance):
    """This reads sample.txt and uses a for loop to replace each
    character by reading the character's value and adding that by one
    to give us the character next to it. Each decrypted character is put
    into the new string and printed after it is done."""
    code = ""
    for ch in sample:
        ordvalue = ord(ch)
        if ord('a') <= ordvalue <= ord('z'):
            cipherValue = ordvalue + distance
            if cipherValue > ord('z'):
                cipherValue = ord('a') + distance - (ord('z') - ordvalue +1)
            code += chr(cipherValue)
        else:
            code += ch
    return code

def main():
    f = open("sample.txt",'r')
    plaintext = f.read()
    print('Original:')
    print(plaintext)
    dist = 10
    code=encryption(plaintext,dist)
    print('Encryption:')
    print(code)
    ptext=decryption(code,dist)
    print('Decryption:')
    print(ptext)
    
if __name__== "__main__":
    main()
