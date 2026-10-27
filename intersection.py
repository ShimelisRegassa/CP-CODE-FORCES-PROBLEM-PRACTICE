from collections import  Counter 
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
count=Counter(num1)
res=[]
for i in num2:
    if(count[i]>0):
        res.append(i)
        count[i]-=1
print(*res)
    
