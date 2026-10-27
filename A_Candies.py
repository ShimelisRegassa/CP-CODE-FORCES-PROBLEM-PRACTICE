t=int(input())
for i in range(t):
    b=int(input())
    k=2
    while(k>=2):
        x=b//(2**k-1)
        if(b%(2**k-1)==0):
            print(x)
            break
        k+=1
        