a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    count=0
    for i in range(1,len(data)):
        if(data[i]%data[0]!=0):
            print("NO")
            break
        
        else:
            count+=1
    if(len(data)-1==count):
        print("YES")
    