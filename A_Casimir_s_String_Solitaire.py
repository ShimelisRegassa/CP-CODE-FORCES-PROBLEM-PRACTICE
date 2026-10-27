t=int(input())
for i in range(t):
    name=input()
    num1=name.count("A")
    num2=name.count("B")
    num3=name.count("C")
    if(num2==num1+num3):
        print("YES")
    else:
        print("NO")