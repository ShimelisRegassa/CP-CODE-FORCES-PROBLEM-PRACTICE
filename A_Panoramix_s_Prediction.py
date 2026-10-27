a,b=map(int,input().split())
a=a+1
boo=True
while(boo):
    d=True
    for i in range(2,a):
        if(a%i==0):
            d=False
            break
    if(d):
        break
    a+=1
if(a==b):
    print("YES")
else:
    print("NO")
            
