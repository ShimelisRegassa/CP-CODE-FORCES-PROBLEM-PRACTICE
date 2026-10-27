t=int(input())
for m in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    val=n+1
    res=[]
    for i in range(len(data)):
        res.append(val-data[i])
    print(*res)
    
        
        