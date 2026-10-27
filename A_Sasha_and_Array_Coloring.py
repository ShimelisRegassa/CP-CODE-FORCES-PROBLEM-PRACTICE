t=int(input())
for i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    num.sort()
    left=0
    right=len(num)-1
    sum=0
    while(left<right):
        sum+=(num[right]-num[left])
        left+=1
        right-=1
    print(sum)
        