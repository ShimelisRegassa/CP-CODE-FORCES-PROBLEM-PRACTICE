a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(str,input().split("#")))
    boolean=False
    for i in data:
        if(len(i)>=3):
            boolean=True
            break
    if(boolean):
        print(2)
    else:
        count=0
        for i in data:
            count+=len(i)
        print(count)
    
       