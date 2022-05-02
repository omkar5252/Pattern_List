# Accept a number from user and check if this element is present in the list or not. 
# Also tell how many times it is present in the list.

def linear_search(data,ele):
    n = len(data)
    for i in range(0,n):
        if (data[i] == ele):
            return i
    else:
        return -1
        
data = [1,2,3,4,5,4,2]
ele = int(input("Enter a element tobe search:"))
index = linear_search(data,ele)
if (index == -1):
    print(ele,"is not present in list")
else:
    print(ele,"is present in list.")

for x in set(data):
    if (ele == x):
        print(x,"is present for",data.count(x),"times in a List.")




             


