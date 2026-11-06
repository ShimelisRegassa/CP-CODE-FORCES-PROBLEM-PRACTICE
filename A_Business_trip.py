k=int(input())
num=list(map(int,input().split()))
if(k==0):
    print(0)
else:
    num.sort(reverse=True)
    val=0
    for i in range(len(num)):
        val+=num[i]
        if(val>=k):
            print(i+1)
            break
    else:
        print(-1)