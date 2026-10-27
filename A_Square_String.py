a=int(input())
for i in range(a):
    b=input()
    if(len(b)%2==1):
        print("NO")
    else:
        num1=b[:len(b)//2]
        num2=b[len(b)//2:]
        if(num1==num2):
            print("YES")
        else:
            print("NO")