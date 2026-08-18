a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    num1=len(set(data))
    num2=len(data)
    num3=num2-num1
    if(num3%2==1):
        print(num1-1)
    else:
        print(num1)
        
    