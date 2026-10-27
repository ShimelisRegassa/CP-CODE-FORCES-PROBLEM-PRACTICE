a=int(input())
num=list(map(int,input().split()))
data=[]
total=0
for i in range(len(num)):
    total+=num[i]
    data.append(total)
print(*data)
            3, 1, 7, 0, 4, 1, 6