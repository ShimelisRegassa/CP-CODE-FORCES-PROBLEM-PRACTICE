import math
t=int(input())
for i in range(t):
    b=int(input())
    n=input()
    num1=math.sqrt(b)
    num2=int(num1)
    if(num1!=num2):
        print("No")
    else:
        for i in range(b):
            row=i//num2
            col=i%num2
            boolean= row==0 or row==num2-1 or col==0 or col==num2-1
            if(boolean):
                if(n[i]!="1"):
                    print("No")
                    break
            else:
                if(n[i]!="0"):
                    print("No")
                    break
        else:
            print("Yes")
               
               
            
        
    