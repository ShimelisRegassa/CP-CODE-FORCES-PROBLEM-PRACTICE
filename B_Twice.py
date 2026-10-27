t=int(input())
for i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    num.sort()
    counter=0
    left=0
    right=1
    while(right<b):
        if(num[left]==num[right]):
            counter+=1
            right+=2
            left+=2
        else:
            right+=1
            left+=1
    print(counter)
