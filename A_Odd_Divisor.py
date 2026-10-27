a=int(input())
for i in range(a):
    num=int(input())
    if( num%2==1):
        print("YES")
    else:
        c=num//2
        while(c>1):
            if(c%2==1):
                print("YES")
                break
            c=c//2
        if(c==1 ):
            print("NO")
                
            
                
                
            
    