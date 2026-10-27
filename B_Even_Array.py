a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    count1=0
    count2=0
    for i in range(len(data)):
        if(data[i]%2==i%2):
            continue
        elif(data[i]%2==0 and i%2==1):
            count1+=1
        else:
            count2+=1
    if(count1==count2):
        print(count1)
    else:
        print(-1)
            