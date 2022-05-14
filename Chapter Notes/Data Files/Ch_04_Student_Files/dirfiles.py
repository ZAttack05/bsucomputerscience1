import os
currentDirectoryPath = os.getcwd()
print(currentDirectoryPath)
listOfFileNames = os.listdir(currentDirectoryPath)
listOfFileNames.sort()
for name in listOfFileNames:
	if ".py" in name:
	    print(name)

print("sep:", os.sep)
