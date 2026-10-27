a,b=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
current=0
left=0
for i in range(a):
    while(left<b-1 and abs(num2[left+1]-num1[i])<=abs(num2[left]-num1[i]) ):
        left+=1
    rel=abs(num2[left]-num1[i])
    current=max(current,rel)
print(current)
    
