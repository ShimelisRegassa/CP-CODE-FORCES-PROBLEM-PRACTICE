a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    num1=input()
    num2=input()
    counter = 0
    boolean=True
    while num2 not in num1:
        if(len(num1)>b*c):
            boolean=False
            break
        else:
            num1+=num1
            counter+=1
            
    if(boolean):
        print(counter)
    else:
        print(-1)
   
  
  
                    
        