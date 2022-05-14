def mean(lyst):
    sm=0
    for num in lyst:
        sm += num
    length=len(lyst)
    if length == 0:
        return None
    return sm / length


def openFile():
    fname = input("Enter a file name: ")
    f=open(fname, 'r')
    return f

def readFile(fname):
    '''
    read a file of numbers, return a list of values
    '''
    #f=open(fname,'r') # returns a file object

    f=openFile()
    fstring = f.read()

    f.close()
    
    #print(fstring)
    l = fstring.split()
    #print(l)
    lyst=[]
    for word in l:
        lyst.append(float(word))
    #print(lyst)
    return lyst

def getInput():
    n=int(input("How many values do you want?"))
    l=[]
    for i in range(n):
        l.append(int(input("Enter a value:")))
    return l

def output(l, ave):
    print(l)
    print("average is", ave)
    
def main():
    #li=getInput()
    #average = mean(li)
    #output(li, average)
    li=readFile("numbers.txt")
    average = mean(li)
    output(li, average)

if __name__ == "__main__":
    main()
