a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    maximum=0
    summation=0
    counter=0
    for i in data:
        summation+=i
        if(i>maximum):
            maximum=i
        if(summation ==2*maximum):
            counter+=1
    print(counter)