a=int(input())
data=list(map(int,input().split()))
length=0
num=set(data)
for i in num:
    if i-1 not in num:
        ele=i
        count=1
        while ele+1 in num:
            count+=1
            ele+=1
        length=max(length,count)
print(length)
            
            