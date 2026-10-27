t=int(input())
for i in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    num1=max(data)
    num2=min(data)
    b,c,d,e=0,0,0,0
    for i in range(len(data)):
        if(data[i]==num1):
            c=i+1
            b=n-i
        elif(data[i]==num2):
            d=i+1
            e=n-i
    fir=min(b,c)
    sec=min(d,e)
    res1=fir+sec
    res2=max(c,d)
    res3=max(b,e)
    print(min(res1,res2,res3))
