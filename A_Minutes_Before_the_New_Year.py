a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if(c>0):
        num1=23-b
        num2=60-c
        print(((num1)*60)+num2)
    else:
        print((24-b)*60)