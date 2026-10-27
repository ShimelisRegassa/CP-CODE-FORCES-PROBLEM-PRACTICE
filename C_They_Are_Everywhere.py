n=int(input())
data=input()
counter=float("inf")
count={}
right=0
left=0
while(right<len(data)):
    count[data[right]]=count.get(data[right],0)+1
    while(len(count)==len(set(data))):
        count[data[left]]-=1
        counter=min(counter,right-left+1)
        if(count[data[left]]==0):
            del count[data[left]]
        left+=1
    right+=1
print(counter)