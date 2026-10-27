n=int(input())
num=list(map(int,input().split()))
num.sort()
counter=0
val=0
total=sum(num)
for i in range(n-1,-1,-1):
    val+=num[i]
    counter+=1
    if(val>total-val):
        print(counter)
        break


    
    
    
    
