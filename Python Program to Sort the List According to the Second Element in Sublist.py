# Python Program to Sort the List According to the Second Element in Sublist
# Bubble sort method is used

data = [[1,8],[2,2],[3,5]]
print("Original list:",data)
n = len(data)

for j in range(1,n):
    for i in range(0,n-j):
        if (data[i][1] > data[i+1][1]):
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
print("Sorted list:",data)
