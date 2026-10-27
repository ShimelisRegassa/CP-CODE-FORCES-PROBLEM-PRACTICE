a=int(input())
for i in range(a):
    c=int(input())
    num=input()
    vo="ae"
    num1=[]
    l=c-1
    while(l>=0):
        if(num[l] in vo):
            b=num[l-1:l+1]
            num1.append(b)
            l-=2
        
        else:
            b=num[l-2:l+1]
            num1.append(b)
            l-=3
    num1.reverse()
    print(".".join(num1))