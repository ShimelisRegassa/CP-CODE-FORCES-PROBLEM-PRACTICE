a=int(input())
for i in range(a):
    b=int(input())
    if(b>2 and b%2==1):
        print(0)
    else:
        count=0
        i=0
        while(i<=b):
            if(i%2==0 and (b-i)%4==0):
                count+=1
            i+=2
        print(count)
        
            
            
            