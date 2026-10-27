t=int(input())
for i in range(t):
    s=input()
    res=float("inf")
    for i in s:
        res=min(res,int(i))
    print(res)