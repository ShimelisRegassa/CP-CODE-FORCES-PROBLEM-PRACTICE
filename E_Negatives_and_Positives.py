t=int(input())
for i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    count2=0
    res1=min(num)
    val=0
    res2=float("inf")
    summation=0
    for i in range(b):
        if(num[i]<0):
            count2+=1
            res1=max(res1,num[i])
        else:
            if(num[i]==0):
                val=1
            else:
                res2=min(res2,num[i])
    for i in num:
        summation+=abs(i)
            
    if(count2%2==0):
        print(summation)
    else:
        if(val!=0):
            print(summation)
        else:
            if(abs(res1)>res2):
                print(summation -(2*res2))
            else:
                print(summation+(2*res1))
    
        
        
            
    

                
            