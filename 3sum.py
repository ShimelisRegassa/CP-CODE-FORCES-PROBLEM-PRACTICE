data=list(map(int,input().split()))
num=[]
data.sort()
for i in range(len(data)-2):
    va=data[i]
    if(i>0 and data[i]==data[i+1]):
        continue
    va=-va
    right=len(data)-1
    left=i+1
    while(left<right):
        if(data[left]+data[right]<va):
            left+=1
        elif(data[left]+data[right]>va):
            right-=1
        else:
            b=[data[right],data[left],va]
            num.append(b)
            while(left<right and data[left]==data[left+1]):
                left+=1
            while(left<right and data[right]==data[right-1]):
                right-=1
            right-=1
            left+=1
print(num)
            
         