import math
n=int(input())
size=1000003
data=list(map(int,input().split()))
check=[True]*size
check[0]=check[1]=False
for i in range(2,int(size**0.5)):
    if(check[i]==True):
        for j in range(i*i,size,i):
            check[j]=False
res=[]
for j in data:
    r=int(j**0.5)
    if(r*r==j and check[r]==True):
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res))
    

        