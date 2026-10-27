t=int(input())
for j in range(t):
    a,b,c=map(int,input().split())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    known=sum(num2)
    total=a*(a+1)//2
    ans=""
    if(a==c):
        print("1"*b)
    elif(c==a-1):
        absent=total-known
        for i in num1:
            if(absent==i):
                ans+="1"
            else:
                ans+="0"
        print(ans)
    else:
        print("0"*b)