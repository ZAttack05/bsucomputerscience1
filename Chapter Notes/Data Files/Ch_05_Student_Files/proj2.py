'''
This is the implementation of project 2 on page 165
'''

def inputLineNumber(numOfLines):
    lineNum = int(input("Enter a valid line number:"))
    while lineNum < 0 or lineNum > numOfLines:
        lineNum = int(input("Enter a valid line number:"))
    return lineNum
    
def main():
    fname = input("Please enter a text file name:")
    f = open(fname, 'r')
    lineList=[]
    for line in f:
        lineList.append(line)
    numOfLines = len(lineList)
    print("Number of lines:", numOfLines)
    lineNum = inputLineNumber(numOfLines)
        
    while lineNum != 0:
        print(lineList[lineNum-1])
        print("Number of lines:", numOfLines)
        lineNum = inputLineNumber(numOfLines)

if __name__ == "__main__":
    main()
