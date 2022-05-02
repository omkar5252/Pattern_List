# Python Program to Find the Intersection of Two List

l1 = [1,5,4]
l2 = [5,4,2,7,9,8]
intersection = []

for x in l1:
    if (x in l2):
        intersection = intersection + [x]
print("Intersecion of two list:",intersection)



