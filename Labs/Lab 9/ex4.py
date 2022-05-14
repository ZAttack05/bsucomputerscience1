import time
import unorderedlist

print("The list will be 5 items long, with the items 1, 3, 2, 5, 4. These are the results for each.")

'''This is the initializing test.'''
#For regular list
print("\n")
bc = time.time()
list = [1, 3, 2, 5, 4]
ad = time.time()
ft = ad - bc
print ("The time it took to initialize your list was " + str(ft))

#For linked list
bc = time.time()
llist = unorderedlist.UnorderedList()
llist.add(4)
llist.add(5)
llist.add(2)
llist.add(3)
llist.add(1)
ad = time.time()
ft = ad - bc
print ("The time it took to initialize your linked list was " + str(ft))

'''This is the test for adding an item to the beginning of the list, since linked list cannot add to the end without a special function.'''

#Test for regular list.
print("\n")
bc = time.time()
i = 1
item = 6
previous = list[0]
list[0] = item
while i < len(list):
    current = list[i]
    list[i] = previous
    previous = current
    i += 1
if i <= len(list):
    list.append(previous)
ad = time.time()
ft = ad - bc
print("The time it took to add an item to the begginning of the list, without losing any data was " + str(ft))

#Test for linked list
bc = time.time()
llist.add(item)
ad = time.time()
ft = ad - bc
print("The time it took to add an item to the begginning of the linked list, without losing any data was " + str(ft))

'''This is a test to see how long it takes to look for an item in the list.'''

value = 3
#Test for regular list
print("\n")
bc = time.time()
found = False
for i in range(len(list)):
    if list[i] == value:
        found = True
        break
print(found)
ad = time.time()
ft = ad - bc
print("The time it took to find this item in a list was " + str(ft))

#Test for linked list
print("\n")
bc = time.time()
print(llist.search(3))
ad = time.time()
ft = ad - bc
print("The time it took to find this item in a linked list was " + str(ft))

'''This is the test for removing an item, with the assumption that the item is there.'''
value = 3
print("\n")
#Test for list
bc = time.time()
i = 0
while True: #I did a while true statement, because in a linked list if the item is not there, it will search until it is out of range.
    if list[i] == value:
        list.pop(i)
        break
    else:
        i += 1
ad = time.time()
ft = ad + bc
print("The time it took to remove this item in a list was " + str(ft))

#Test for a linked list
bc = time.time()
llist.remove(3)
ad = time.time()
ft = ad - bc
print("The time it took to remove this item in a linked list was " + str(ft))



