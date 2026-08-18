a=int(input())
for i in range(a):
    b=int(input())
    path=input()
    x=0
    y=0
    for i in range(len(path)):
        if(path[i]=="U"):
            y+=1
        elif(path[i]=="D"):
            y-=1
        elif(path[i]=="R"):
            x+=1
        else:
            x-=1
        if(x==1 and y==1):
            print("YES")
            break
    else:
        print("NO")