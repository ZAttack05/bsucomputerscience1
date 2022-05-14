def mergeSort(lyst):
    copyBuffer = list(lyst)
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    if low < high:
        middle = (low+high)//2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle+1, high)
        merge(lyst, copyBuffer, low, middle, high)
        print(lyst)

def merge(lyst, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle +1

    for i in range(low, high+1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1
    for i in range(low, high+1):
        lyst[i] = copyBuffer[i]

l=[8,5,3,6,12,4, 33, 24, 13, 21, 1, 40, 7, 36, 15, 9]
mergeSort(l)
print(l)
