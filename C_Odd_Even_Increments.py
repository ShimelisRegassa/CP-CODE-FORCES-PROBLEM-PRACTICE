a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    num1=[]
    num2=[]
    for i in range(len(data)):
        if(i%2==1):
            num1.append(data[i]%2)
        else:
            num2.append(data[i]%2)
    if(len(set(num1))==1 and len(set(num2))==1):
        print("YES")
    else:
        print("NO")
    