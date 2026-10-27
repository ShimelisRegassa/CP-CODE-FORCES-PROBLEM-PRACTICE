a,b=map(int,input().split())
data=list(map(int,input().split()))
counter=0
for i in data:
    if(i>b):
        counter+=2
    else:
        counter+=1
print(counter)