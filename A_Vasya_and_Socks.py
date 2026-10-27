a,b=map(int,input().split())
counter=0
i=1
num=1
counter=0
while(num<=a):
    counter+=1
    if(i%b==0):
        a+=1
    i+=1
    num+=1
print(counter)

    