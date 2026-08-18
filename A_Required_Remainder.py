a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    num=d%b
    if(num>=c):
        out=d-(num-c)
        print(out)
    else:
       total=(d//b)*b-(b-c)
       print(total)