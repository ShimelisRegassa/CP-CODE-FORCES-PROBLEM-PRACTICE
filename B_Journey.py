t=int(input())
for i in range(t):
    n,b,c,d=map(int,input().split())
    num1=b+c+d
    quo=n//num1
    num2=n%num1
    if(num2):
        if(num2<=b):
            print(3*quo +1)
        elif(num2>b and num2<=(b+c)):
            print(3*quo +2)
        else:
            print(3 *quo +3)
        
    else:
        print(3*quo)
        
    

   
        
    