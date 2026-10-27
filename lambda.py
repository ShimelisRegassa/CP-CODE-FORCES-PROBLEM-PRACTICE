
from collections import Counter
lst=list(map(int,input().split()))
k=int(input())
num=Counter(lst)
x=num.items()
val=sorted(x,key=lambda x:-x[1])
for i in range(k):
    print(val[i][0],end="  ")
