a,b,c=map(int,input().split())
n=0
for i in range(1,c+1):
    n+=(a*i)
if(n>b):
    print(n-b)
else:
    print(0)