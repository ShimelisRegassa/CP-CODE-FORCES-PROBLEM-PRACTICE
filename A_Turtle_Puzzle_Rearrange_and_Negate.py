a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    sum1=0
    for i in data:
        sum1+=(abs(i))
    print(sum1)
        
        