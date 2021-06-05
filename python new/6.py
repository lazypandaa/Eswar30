#                        Lists in Python

[]                            # list with no member, empty list
[1, 2, 3]                     # list of integers 
[1, 2.5, 3.7, 9]              # list of numbers (integers and floating point)
['a', 'b', 'c']               # lisst of characters
['a', 1, 'b', 3.5, 'zero']    # list of mixed value types
['One', 'Two', 'Three']       # list of strings 

# List Methods :
l1=[1,8,4,3,15,20,25,89,65]       #l1 is a list
print(l1)

l1.sort()
print(l1)      #l1 after sorting
l1.reverse()
print(l1)      #l1 after reversing all elements

# List Methods :- 
list1=[1,2,3,6,7,5,4]     #list1 is a list

list1.append(7)    # This will add 7 in the last of list 
list1.insert(3,8)    # This will add 8 at 3 index in list
list1.remove(1)    #This will remove 1 from the list 
list1.pop(2)          #This will delete and return index 2 value.

# Tuples in Python :
a=()    # It's an example of empty tuple
x=(1,)   # Tuple with single value i.e. 1 
tup1 = (1,2,3,4,5)
tup1 = ('harry', 5, 'demo', 5.8)

# Swapping of two numbers :
a = 10 
b = 15
print(a,b)     #It will give output as: 10 15
a,b = b,a 
print(a,b)     #It will give output as: 15 10
