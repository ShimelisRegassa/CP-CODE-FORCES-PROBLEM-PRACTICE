a=int(input())
for i in range(a):
    b=int(input())
    if((b//2)%2==1):
        print("NO")
    else:
        data1=[]
        data2=[]
        for i in range(1,b//2 +1):
            data1.append(2*i)
        for i in range(1,b//2):
            data2.append((2*i)-1)
        num1=sum(data1)
        num2=sum(data2)
        data2.append(num1-num2)
        data1.extend(data2)
        print("YES")
        print(" ".join(str(i) for i in data1))
        
        
    