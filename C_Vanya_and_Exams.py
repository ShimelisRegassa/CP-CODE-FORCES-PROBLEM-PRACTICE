a,b,c =map(int,input().split())
total=0
exam=[]
count=0
for i in range(a):
    m,e=map(int,input().split())
    exam.append([m,e])
    total+=m
required=c*a -total
if(required<=0):
    print(0)
else:
    exam.sort(key=lambda x:x[1])
    for x,y in exam:
        left=b-x
        take=min(required,left)
        required-=take
        count+=(take*y)
        if(required<=0):
            break
        else:
            continue
    print(count)
        
        
    
  
    
    
        
    

