num=input().split()
a=int(num[0])
b=int(num[1])
data=[]
counter=0
for i in range(a):
    v=input()
    data.append(v)
check=set()
for i in range(a):
    for j in range(b):
        if(i==0):
            if(data[0][j]==num[2]):
                if(i+1<a):
                    check.add(data[i+1][j])
                else:
                    check.add(data[i][j-1])
                    if(j+1<b):
                        check.add(data[i][j+1])
                if(j==0 and j+1<b):
                    check.add(data[i][j+1])
                else:
                    check.add(data[i][j-1])
                    if(j+1<b):
                        check.add(data[i][j+1])
            
        else:
            if(data[i][j]==num[2]):
                check.add(data[i-1][j])
                if(i+1<a ):
                    check.add(data[i+1][j])
                if(j==0 and j+1<b):
                    check.add(data[i][j+1])
                else:
                    check.add(data[i][j-1])
                    if(j+1<b):
                        check.add(data[i][j+1])              
check.discard(".")
check.discard(num[2])
print(len(check))
                        
                
            
                    
                    
        
        

            
    

