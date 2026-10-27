a=int(input())
for i in range(a):
    b=int(input())
    if(b%2==0):
        num=b//2 -1
        print((2*num)+1)
    else:
        num=b//2
        print(2*num)