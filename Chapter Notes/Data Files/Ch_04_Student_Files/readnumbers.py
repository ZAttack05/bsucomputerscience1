f = open("integers.txt", 'r')
theSum = 0
count = 0
for line in f:
    wordlist = line.split()
    for word in wordlist:
        count += 1
        number = int(word)
        theSum += number
print("The sum is", theSum, "Total number of integers is", count)
print("The average is:", theSum/count)
