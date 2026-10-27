def count(data,tar):
    right=len(data)-1
    left=0
    counter=0
    while(left<right):
        val=data[right]+data[left]
        if( val<=tar):
            counter+=(right-left)
            left+=1
        else:
            right-=1
    return counter
t=int(input())
for i in  range(t):
    a,b,c=map(int,input().split())
    data=list(map(int,input().split()))
    data.sort()
    total=sum(data)
    upper=total-b
    lower=total-c
    print(count(data,upper)-count(data,lower-1))
    


            
        