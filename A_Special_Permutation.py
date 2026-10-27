a=int(input())
for i in range(a):
    b=int(input())
    data=[]
    if(b%2==0):
        for i in range(b,0,-1):
            data.append(i)
        print(*data)
    else:
        for i in range(b,0,-1):
            data.append(i)
        mid=b//2 
        data[mid],data[0]=data[0],data[mid]
        print(*data)
        
        