a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    data=list(map(int,input().split()))
    count=0
    data.sort(reverse=True)
    power=0
    for i in data:
        if(i * 2**power>c):
            count+=1
        else:
            power+=1
    print(count)
            
        
    
        