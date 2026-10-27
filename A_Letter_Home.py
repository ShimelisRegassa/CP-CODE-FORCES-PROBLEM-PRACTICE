t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    num=list(map(int,input().split()))
    num1=min(num)
    num2=max(num)
    if(num1<b and num2>b):
        if((num2-b)>(b-num1)):
            print(2*(b-num1)+(num2-b))
        else:
             print(2*(num2-b)+(b-num1))
            
    elif(b>=num2):
        print(b-num1)
    else:
        print(num2-b)
