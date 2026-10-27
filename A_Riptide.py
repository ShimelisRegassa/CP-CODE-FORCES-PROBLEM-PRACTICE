t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    counter=0
    boolean=True
    while(boolean):
        if(a==b or  b==c or a==c):
            break
        lst=[a,b,c]
        e=max(lst)
        d=min(lst)
        val=0
        for i in lst:
            if(i!=e and i!=d):
                val=i
                break
        e-=1
        d+=1
        counter+=1
        a,b,c=d,val,e
    print(counter)
        
    
         
        
  
        
        
        
        