a,b=map(int,input().split())
counter=0
for i in range(a):
    c=input().split()
    if(c[0]=="+"):
        num=int(c[1])
        b+=num
    else:
        num=int(c[1])
        if(b>=num):
            b-=num
        else:
            counter+=1
print(b,counter)
        
    