nums=list(map(int,input().split()))
b=int(input())
total=0
counter=0 
dict={0:1}
for i in nums:
    total+=i
    if(total-b in dict):
        counter+=dict[total-b]
    dict[total]=dict.get(total,0)+1
print(counter)