
n,m=map(int,input().split())
num=list(map(int,input().split()))
check=[]
for i in num:
    if(len(check)==m and i not in check):
        check.pop(0)
    if(i  in check):
        continue
    check.append(i)
check.reverse()
print(len(check))
print(*check)