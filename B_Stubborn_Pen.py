t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    flag=True
    counter=0
    for i in s:
        if(flag):
            if(i=="B"):
                counter+=1
            else:
                flag=False
        else:
            if(i=="R"):
                counter+=1
            else:
                flag=True
    print(counter)
    