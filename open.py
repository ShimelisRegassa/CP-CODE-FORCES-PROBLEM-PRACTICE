nums=list(map(int,input().split()))
k=int(input())
dict={0:-1}
current=0
counter=0
for i in range(len(nums)):
    val=nums[i]
    current+=val
    if((current-k) in dict):
        if(current-k==0 and dict[0]==-1):
            dict[0]=1         
        counter+=dict[current-k]
    dict[current]=dict.get(current,0)+1
        
print(counter)
print(dict[current])