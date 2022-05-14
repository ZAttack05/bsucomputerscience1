'''This function uses recursion to reverse te order of a list.'''
def reverse(l):
    if len(l) == 0: #Base case
        return []
    else:
        return l[-1:] + reverse(l[:-1]) #Recurisve call

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The original list:", list)
print("Reversed list:", reverse(list))
