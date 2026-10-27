a=int(input())
data1=list(map(int,input().split()))
b=int(input())
data2=list(map(int,input().split()))
num=[]
for i in range(len(data2)):
    left=0
    while(left<len(data1)):
        if(data1[left]>=data2[i]):
            num.append(left)
            break
        left+=1
    if(left==len(data1)):
        num.append(left)
print(*num)
            
