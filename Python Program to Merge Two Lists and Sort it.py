# Python Program to Merge Two Lists and Sort it

l1 = [6,9,7,3,4,2,1]
l2 = [13,16,19,25,38,10]

l3 = l1 + l2

print("List 1:",l1)
print("List 2:",l2)
print("Merge list:",l3)

for i in range(0,len(l3)):
    min = l3[i]
    index = i

    for j in range(i+1,len(l3)):
        if (min > l3[j]):
            min = l3[j]
            index = j
    l3[i],l3[index] = l3[index],l3[i]
    
print("sorted list:",l3)
