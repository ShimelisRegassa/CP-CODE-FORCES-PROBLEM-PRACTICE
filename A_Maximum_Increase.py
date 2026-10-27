a=int(input())
data=list(map(int,input().split()))
count=1
counter=1
for i in range(1,len(data)):
    if(data[i]>data[i-1]):
        count+=1
    else:
        count=1
    if(counter<count):
        counter=count
print(counter)