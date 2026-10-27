num=list(map(int,input().split()))
case2=0
case1=1
num.sort()
for i in range(3,-1,-1):
    right=i-1
    left=0
    boolean=False
    while(left<right):
        if(num[left]+num[right]>num[i]):
            boolean=True
            break
        elif(num[left]+num[right]==num[i]):
            case2=1
            left+=1
        else:
            left+=1     
    if(boolean):
        print("TRIANGLE")
        case1=0
        break
if(case1 and case2):
    print("SEGMENT")
elif(case1):
    print("IMPOSSIBLE")
            
            