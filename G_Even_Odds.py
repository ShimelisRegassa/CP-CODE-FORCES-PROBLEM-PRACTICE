a,b=map(int,input().split())
if(a%2==0):
    num=a//2
    if(b<=num):
        print(2*b-1)
    else:
        print(2*(b-num))
    
else:
    num1=a//2
    if(b<=num1+1):
        print(2*b-1)
    else:
        print(2*(b-num1-1))
        
    
    
    
    