# Problem no 5 : Python Program to Sort a List According to the Length of the Elements 
# within the list.

list = ["bicycle","truck","car"]
print("Original list:",list)

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if (len(list[i]) > len(list[j])):
            list[i],list[j] = list[j],list[i]
            
print("Sorted list:",list)




