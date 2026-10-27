a=int(input())
for i in range(a):
    b=int(input())
    num=input()
    c=int(input())
    num2=input()
    num3=input()
    data=[]
    for i in range(len(num3)):
        if(num3[i]=="D"):
            num+=num2[i]
        else:
            data.append(num2[i])
    data.reverse()
    out="".join(data)
    print(out+num)
        
    
    