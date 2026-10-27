t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    data1=sorted(num1)
    data2=sorted(num2)
    val=0
    if(a==b):
        print(data2[0]*a)
    else:
        val=data2[:b]
        