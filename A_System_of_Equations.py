import math 
a,b=map(int,input().split())
count=0
for i in range(int(math.sqrt(a))+1):
    boolean=False
    for j in range(int(math.sqrt(b))+1):
        if(i**2 +j ==a and j**2 +i==b):
            count+=1           
print(count)