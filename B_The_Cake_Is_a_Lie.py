a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    num1=(b-1)
    num2=(c-1)*(num1+1)
    tot=num1+num2
    if(tot==d):
        print("YES")
    else:
        print("NO")