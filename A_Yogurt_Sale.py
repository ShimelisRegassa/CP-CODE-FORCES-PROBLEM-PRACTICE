a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if(b%2==0):
        e=d/2
        if(e>c):
            print(b*c)
        else:
            print((b//2) *d)
    else:
        e=d/2
        if(e>c):
            print((b-1)*c+c)
        else:
            print(((b-1)//2)*d +c)
        