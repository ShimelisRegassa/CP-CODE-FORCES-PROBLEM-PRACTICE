a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    data.sort()
    count=0
    for i in range(1,len(data)):
        count+=data[i]-data[0]
    print(count)