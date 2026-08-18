import math
a=int(input())
for i in range(a):
    b=input()
    num=int(b)
    out=math.sqrt(num)
    num1=int(out)
    if(out==num1):
        print(0,num1)
    else:
        print(-1)
    