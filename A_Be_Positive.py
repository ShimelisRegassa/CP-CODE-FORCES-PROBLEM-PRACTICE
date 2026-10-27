t=int(input())
for i in range(t):
    b=int(input())
    data=list(map(int,input().split()))
    num1=data.count(-1)
    num2=data.count(0)
    if(num1%2==1):
        print(2+num2)
    else:
        print(num2)