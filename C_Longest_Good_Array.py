t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    n=1
    long=0
    while(a<=b):
        long+=1
        a+=n
        n+=1
    print(long)
        
        