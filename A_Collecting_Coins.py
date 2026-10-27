t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    num=max(a,b,c)
    diff=(num-a)+(num-b)+(num-c)
    num1=d-diff
    if(num1%3==0 and num1>=0):
        print("YES")
    else:
        print("NO")