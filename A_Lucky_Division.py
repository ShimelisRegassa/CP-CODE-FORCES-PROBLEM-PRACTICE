a=input()
num1=a.count("4")
num2=a.count("7")
if(len(a)==num1+num2):
    print("YES")
else:
    c=int(a)
    if(c%4==0 or c%7==0 or c%47==0 or c%74==0 ):
        print("YES")
    else:
        print("NO")