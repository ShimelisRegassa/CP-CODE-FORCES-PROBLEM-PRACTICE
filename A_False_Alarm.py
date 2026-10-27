t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    num=list(map(int,input().split()))
    fir=0
    last=0
    for i in range(len(num)):
        if(num[i]==1):
            fir=i
            break
    for i in range(len(num)-1,-1,-1):
            if(num[i]==1):
                last=i  
                break   
    if(last-fir+1<=b):
        print("YES")
    else:
        print("NO")
        
        