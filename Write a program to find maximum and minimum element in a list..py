# Write a program to find maximum and minimum element in a list.

data = [40,50,30,10,20]
min = data[0]
max = data[0]
for i in range(0,len(data)):
    if (min > data[i]):
        min = data[i]
    if (max < data[i]):
        max = data[i]
print("Minimum element in list:",min)
print("Maximum element in list:",max)
