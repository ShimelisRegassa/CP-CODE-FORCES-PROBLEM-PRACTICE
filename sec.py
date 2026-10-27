data=list(map(int,input().split()))
k=int(input())
dict={0:1}
total=0
counter=0
for i in data:
    total+=i
    rem=total%k
    if(rem in dict):
        counter+=dict[rem]
    dict[rem]=dict.get(rem,0)+1
print(counter)