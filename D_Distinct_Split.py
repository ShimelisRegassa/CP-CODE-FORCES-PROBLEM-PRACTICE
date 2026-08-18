t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    counter=0
    num1=set()
    num2=set()
    arra1=[]
    arra2=[]
    left=0
    right=b-1
    total=0
    val=0
    while(left<b and right>-1):
        if(s[left] not in num1):
            num1.add(s[left])
            total+=1
            arra1.append(total)
        else:
            arra1.append(total)
        if(s[right]not in num2):
            val+=1
            num2.add(s[right])
            arra2.append(val)
        else:
            arra2.append(val)
        right-=1
        left+=1
    arra2.reverse()
    for i in range(b-1):
        counter=max(counter,arra1[i]+arra2[i+1])
    print(counter)
            