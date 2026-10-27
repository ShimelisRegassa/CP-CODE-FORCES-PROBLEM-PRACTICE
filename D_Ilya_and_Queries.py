s=input()
t=int(input())
num=[0]*(len(s))
total=0
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        total+=1
        num[i]=total
        
    else:
        num[i]=total
for j in range(t):
    a,b=map(int,input().split())
    if(a==1):
        print(num[b-2])
    else:
        print(num[b-2]-num[a-2])

    