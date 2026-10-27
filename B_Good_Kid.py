import math
a=int(input())
for i in range(a):
    b=int(input())
    lst=list(map(int,input().split()))
    c=min(lst)
    for i in range(len(lst)):
        if(c==lst[i]):
            lst[i]+=1
            break
    print(math.prod(lst))
 