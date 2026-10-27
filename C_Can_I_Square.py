import math
a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    add=sum(data)
    num1=math.sqrt(add)
    num2=int(num1)
    if(num1==num2):
        print("YES")
    else:
        print("NO")
