t=int(input())
for i in range(t):
    n=int(input())
    if(n==3):
        print(-1)
    else:
        if(n%2==0):
            data=[]
            for i in range(1,n+1):
                data.append(i)
            data.reverse()
            print(*data)
        else:
            if(n==5):
                print(5,4,1,2,3)
            else:
                
                data=[]
                for i in range(1,n+1):
                    data.append(i)
                data.reverse()
                data[len(data)//2],data[len(data)//2 +1]= data[len(data)//2 +1],data[len(data)//2]
                print(*data)
            