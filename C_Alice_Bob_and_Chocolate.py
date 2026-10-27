a=int(input())
num=list(map(int,input().split()))
sum1=0
sum2=0
right=a-1
left=0
val1=0
val2=0
while(left<=right):
    if(sum1>sum2):
        sum2+=num[right]
        val2+=1
        right-=1
    elif(sum1<sum2):
        sum1+=num[left]
        val1+=1
        left+=1
    else:
        sum1+=num[left]
        val1+=1
        left+=1
print(left,(5-right)+(right-left))
    
        
        
    