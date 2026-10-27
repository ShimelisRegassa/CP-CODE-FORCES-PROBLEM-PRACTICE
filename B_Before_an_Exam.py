a,b=map(int,input().split())
data=[]
num1=0
num2=0
for i in range(a):
    c,d=map(int,input().split())
    data.append([c,d])
    num1+=c
    num2+=d
num=[]
for i in range((a)):
    num.append(data[i][0])
leftover=b-num1
if(b>=num1 and b<=num2):
    print("YES")
    for i in range(a):
        add=data[i][1]-num[i]
        add=min(leftover,add)
        num[i]+=add
        leftover-=add
        if(leftover==0):
             break
    print(*num)
else:
    print("NO")

