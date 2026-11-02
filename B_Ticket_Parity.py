t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    even=0
    odd=0
    for i in range(n):
        if(i%2==0 and num[i]%2==1):
            even+=1
        elif(i%2==1 and num[i]%2==0):
            odd+=1
    if(odd==even):
        print(even)
    else:
        print(-1)
            
            
        
        
    