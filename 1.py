# Problem no 1: Python Program to Put Even and Odd elements of a List into two Different Lists

data =[1,2,3,4,5,6,7,8,9,10]
size = len(data)
for i in range(1,size):
    even = []
    odd  = []
    for j in data:
        if (j % 2 == 0):
            even = even + [j]
        else:
            odd = odd + [j]
            
print("Even list:",even)
print("Odd list:",odd)
