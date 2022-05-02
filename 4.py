# Problem 4 : Write a program to reverse the list.

data = [1,2,3,4,5]
print("Original List:",data)

n = len(data)
for j in range(1,n):
    for i in range(0,n-j):
        if (data[i] < data[i+1]):
            data[i],data[i+1] = data[i+1],data[i]
print("Reverse List:",data)