a=int(input())
data=list(map(int,input().split()))
num=[]
for i in range(len(data)-1,-1,-1):
    if(data[i] not in num):
        num.append(data[i])
num1=num[::-1]
print(len(num1))
print(*num1)