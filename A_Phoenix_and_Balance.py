a=int(input())
for i in range(a):
    b=int(input())
    data=[]
    num1=0
    for i in range(1,b+1):
        data.append(2**i)
    mid=len(data)//2
    for i in range(mid-1,len(data)-1):
        num1+=data[i]
    num2=sum(data)-num1
    print(abs(num2-num1))
    
        