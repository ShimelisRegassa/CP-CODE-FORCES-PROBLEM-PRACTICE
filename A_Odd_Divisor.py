t=int(input())
for i in  range(t):
    b=int(input())
    if(b%2==1):
        print("YES")
    else:
        num=b//2
        while(num>=3):
            if(num%2==1):
                print("YES")
                break
            num/=2
        if(num<3):
            print("NO")
       