t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    c=a*b
    print(c//2+c%2)