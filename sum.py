a=int(input())
data=list(map(int,input().split()))
num=[]
for i in range(len(data)-2):
    for j in range(i+1,len(data)-1):
        sum=data[i]+data[j]+data[j+1]
        if(sum==0):
            b=[data[i],data[j],data[j+1]]
            num.append(b)
print(num)
