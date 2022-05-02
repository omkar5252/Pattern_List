# Problem no 4 : Python Program to Find the Second Largest Number in a List Using Bubble Sort

data = [10,20,30,40,80]

n = len(data)

for j in range(1,n):
    for i in range(0,n-j):
        if (data[i] > data[i+1]):
            smax = data[i]
            data[i] = data[i+1]
            data[i+1] = smax
result = data[n-2]
print("Second Largest Element:",result)

