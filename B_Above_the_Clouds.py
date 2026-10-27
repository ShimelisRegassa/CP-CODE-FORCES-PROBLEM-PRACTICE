t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    left=1
    boolean=False
    while(left<=b-2):
        c=s[:left]
        d=s[left]
        l=s[left+1:b]
        num1=c+l
        if(d in num1):
            boolean=True
            break
        left+=1
    if(boolean):
        print("Yes")
    
        
    else:
        print("No")
    
        