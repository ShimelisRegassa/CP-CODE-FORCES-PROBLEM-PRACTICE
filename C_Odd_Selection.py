t=int(input())
for i in range(t):
    b,c=map(int,input().split())
    num=list(map(int,input().split()))
    even=0
    odd=0
    for i in range(b):
        if(num[i]%2==0):
            even+=1
        else:
         odd+=1
    n=1 
    boolean=False
    while(n<=odd and n<=c):
        res=c-n
        if(res<=even):
            boolean=True
            break
        n+=2
    if(boolean):
        print("Yes")
    else:
        print("No")
            
    