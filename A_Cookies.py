n=int(input())
num=list(map(int,input().split()))
total=sum(num)
counter=0
for i in num:
    temp=total-i
    if(temp%2==0):
        counter+=1
print(counter)
    