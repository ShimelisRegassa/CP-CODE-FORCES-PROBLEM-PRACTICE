from collections import Counter
t=int(input())
for i in range(t):
    b=int(input())
    data=list(map(int,input().split()))
    fre=Counter(data)
    count=0
    data.sort()
    lis1=[]
    lis2=[]
    lis3=[]
    for i in sorted(fre):
        lis1.append(i)
        if(fre[i]>=2):
            lis2.append(i)
        for j in range(fre[i]-2):
            lis3.append(i)
    lis2.sort(reverse=True)
    res=lis1+lis3+lis2
    print(len(lis1)+len(lis2))
    print(*res)
            
   
    
    