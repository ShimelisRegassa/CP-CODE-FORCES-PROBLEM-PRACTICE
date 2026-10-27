import math
a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    pro=1
    prod=math.prod(data)
    for i in range(b-1):
        pro*=data[i]
        if((prod//pro)==pro):
            print(i+1)
            break
    else:
        print(-1)
        
        