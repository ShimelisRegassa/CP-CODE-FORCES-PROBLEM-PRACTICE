a,b=map(int,input().split())
num=list(map(int,input().split()))
left=0
right=0
val1=0
counter1=0
while(right<a and left<=right):
    val1+=num[right]
    while(val1>b):
        val1-=num[left]
        left+=1
    counter1=max(counter1,right-left+1)
    right+=1
print(counter1)
   
        
        