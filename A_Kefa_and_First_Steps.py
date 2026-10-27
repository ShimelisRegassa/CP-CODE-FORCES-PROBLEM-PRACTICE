a=int(input())
data=list(map(int,input().split()))
count=1
out=1
for i in range(len(data)-1):
    if(data[i]<=data[i+1]):
        count+=1
    else:
        count=1
    if(count>out):
        out=count
print(out)




