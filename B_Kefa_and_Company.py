n,s=map(int,input().split())
data=[]
for i in range(n):
    a,b=map(int,input().split())
    data.append((a,b))
data.sort(key=lambda x:x[0])
left=0
right=0
val=0
res=0
while(right<n and left<n):
    while(data[right][0]-data[left][0]>=s):
        val-=data[left][1]
        left+=1
    val+=data[right][1]
    res=max(res,val)
    right+=1
print(res)
        
    