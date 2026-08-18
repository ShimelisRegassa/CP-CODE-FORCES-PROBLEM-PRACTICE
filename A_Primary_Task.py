t=int(input())
for i in range(t):
    num=input()
    if(len(num)>2):
        b=num[:2]
        if(b=="10"):
            c=int(num[2])
            d=int(num[2:])
            if(c==0):
                print("NO")
            elif(d>=2):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")