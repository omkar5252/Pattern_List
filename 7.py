# Problem 7 : Write a program to create a new list from existing list 
# which contains cube of each number of list.

l1 = []
l2 = [1,2,3,4,5]
print("Original list:",l2)

for i in range(1,len(l2)+1):
    l1= l1 + [(i**3)]
print("cube of list l2:",l1)

    