# Write a program to find the second largest element in the list.

data = [50,30,10,20,80,45]
max = data[0]
smax = 0
for i in range(0,len(data)):
    if (max < data[i]):
        smax = max 
        max = data[i]
    elif (smax < data[i]):
        smax = data[i]
print("Second Largest element in list:",smax)
