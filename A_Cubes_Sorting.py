t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    data=sorted(num)
    if(list(reversed(num))==data and data!=num and len(set(num))==len(num)):
        print("NO")  
    else:
        print("YES")
        