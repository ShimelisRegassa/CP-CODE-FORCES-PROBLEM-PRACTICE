a=int(input())
num=list(map(int,input().split()))
right=len(num)-2
left=1
sum1=num[0]
sum2=num[a-1]
[1,7,3,6,5,6]
while(left<right):
    if(sum1==sum2):
        print(left)
    elif(sum1<sum2):
        sum1+=num[left]
        left+=1
    else:
        sum2+=num[right]
        right-=1
        
    
    
    
    
