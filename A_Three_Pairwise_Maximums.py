a=int(input())
for i in range(a):
    data=list(map(int,input().split()))
    data.sort()
    if(data[1]!=data[2]):
        print("NO")
    else:
        print("YES")
        print(data[2],data[0],data[0])