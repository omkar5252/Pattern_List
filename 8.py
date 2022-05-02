# Problem no 8: Print 1 to 100 in snakes and ladder pattern.

for i in range(10,0,-1):
    x = i * 10
    data = []
    for j in range(0,10):
        data = data + [x-j]

    if (i % 2 != 0):
        data.reverse()
    
    for y in data:
        print(y,end=" ")
    print()