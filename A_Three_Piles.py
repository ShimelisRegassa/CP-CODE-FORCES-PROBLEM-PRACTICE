t=int(input())
for i in range(t):
    if(a==b and b==c):
        print("YES")
    a,b,c=map(int,input().split())
    if((b==a+1 and c==b+1)):
        print("YES")
    else:
        print("NO")
