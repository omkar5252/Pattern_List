# Python Program to Find the Union of two Lists

l1 = [1,2,2,3,5,2,2]
l2 = [5,4,2,4,5]
l3 = []

for x in l1:
    if (x not in l3):
        l3 = l3 + [x]

for x in l2:
    if (x not in l3):
        l3 = l3 + [x]
        
print("Union of two list:",l3)









