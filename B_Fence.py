a,b=map(int,input().split())
num=list(map(int,input().split()))
res=sum(num[:b])
check=res
counter=0
for i in range(b,a):
    res+=num[i]
    res-=num[i-b]
    if(res<check):
        check=res
        counter=i-b+1
print(counter+1)

