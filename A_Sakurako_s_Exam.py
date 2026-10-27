a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    num=b+(c*2)
    if(b%2==1):
        print("NO")
    elif(b%2==0 and c%2==0):
        print("YES")
    elif(b%2==0 and b>0 and c%2==1):
        print("YES")
    else:
        print("NO")
    
      
            