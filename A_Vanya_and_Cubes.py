a=int(input())
count=0
i=1
num=0
while(num<=a):
    num=(i*(i+1))//2
    a-=num
    i+=1
    num+=i
    count+=1
print(count)
    
   

    