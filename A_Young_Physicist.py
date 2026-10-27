a=int(input())
num1=0
num2=0
num3=0
for i in range(a):
    b,c,d=map(int,input().split())
    num1+=b
    num2+=c
    num3+=d
if(num1==0 and num2==0 and num3==0):
    print("YES")
else:
    print("NO")