a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    data=[]
    data=list(map(int,input().split()))
    num1=0
    num2=0
    for i in data:
        if(i%2==0):
            num1+=1
        else:
            num2+=1
    if(num2>=c):
        if(c%2==1):
            print("Yes")
        else:
            if(num1>=1):
                print("Yes")
            else:
                print("No")
    else:
        if(num2%2==1):
            print("Yes")
        else:
            for i in range(1,c+1,2):
                even=c-1
                if(even<=num1 and i<=num2):
                    print("Yes")
                    break
            else:
                print("No")
                    
                    
    
            
        
            
       
        