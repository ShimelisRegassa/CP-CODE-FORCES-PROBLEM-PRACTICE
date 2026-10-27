t=int(input())
for i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    num1=max(num)
    num2=min(num)
    res=num[b-1]-num[0]
    for i in range(b-1):
        res=max(res,num[i]-num[i+1])
    
    aj=num1-num[0]
    res=max(res,aj)
    res=max(res,num[b-1]-num2)
        
    print(res)