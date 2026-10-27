a,b=map(int,input().split())
num=list(map(int,input().split()))
left=0
counter=0
for i in range(a):
    while(num[i]-num[left]>b):
        left+=1
    long=i-left
    counter+=((long)*(long-1)//2)
print(counter)
        
    
    
    
    