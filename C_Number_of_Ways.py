n=int(input())
num=list(map(int,input().split()))
val=sum(num)
if(val%3!=0):
    print(0)
else:
    target=val//3
    sum1=0
    sum2=0
    total=0
    lst=[0]*n
    for j in range(len(num)):
        sum1+=num[j]
        if(sum1==target):
            total+=1
        lst[j]=total
    counter=0
    for j in range(n-1,1,-1):
        sum2+=num[j]
        if(sum2==target):
            counter+=lst[j-2]
    print(counter)
    
            
    