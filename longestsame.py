s=input()
k=int(input())
left=0
right=0
data={}
counter=0
fre=0
while(right<len(s)):
    data[s[right]]=data.get(s[right],0)+1
    fre=max(fre,data[s[right]])
    while((right-left+1)-fre>k):
        data[s[left]]-=1
        left+=1
    counter=max(counter,right-left+1)
    right+=1
print(counter)
    
  
    