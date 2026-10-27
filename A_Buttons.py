a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if(d%2==0):
        num=d//2
        an=b+num
        ka=c+num
        if(an>ka):
            print("First")
        else:
            print("Second")
    else:
        num1=d//2
        num2=d//2 +1
        an=b+num2
        ka=c+num1
        if(an>ka):
            print("First")
        else:
            print("Second")