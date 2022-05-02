# Write a program to remove duplicates from the list.

l1 = []
l2 = [1,3,2,4,2,3,1,5]
print("Original list:",l2)

for x in l2:
    if (x not in l1):
        l1 = l1 + [x]
print("Without duplicate:",l1)
