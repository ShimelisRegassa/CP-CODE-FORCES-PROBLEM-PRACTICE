a=int(input())
for i in range(a):
    b=input()
    if(len(b)>10):
        new=b[0]+str(len(b)-2)+b[len(b)-1]
        print(new)
    else:
        print(b)