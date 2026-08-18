a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    num=max(data)
    print(len(data)*num)