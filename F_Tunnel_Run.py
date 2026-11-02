t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    stack=[]
    counter=0
    for i in s:
        if(i=="("):
            stack.append(i)
        else:
            if(stack):
                stack.pop()
            else:
                counter+=1
    print(counter)
        