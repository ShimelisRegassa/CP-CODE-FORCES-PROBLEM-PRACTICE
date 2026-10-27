t=int(input())
for i in range(t):
    b=int(input())
    data=list(map(int,input().split()))
    num1=data[0]
    num2=data[0]
    boolean=True
    for i in range(1,len(data)):
        if(data[i]==num1-1):
            num1=data[i]
        elif(data[i]==num2+1):
            num2=data[i]
        else:
            boolean=False
            break
            
    if(boolean):
        print("YES")
    else:
        print("NO")
        