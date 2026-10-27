for _ in range(int(input())):
    n=int(input())
    s=input()
    
    eliminated=set()
    stack=[]
    
    for ind,message in enumerate(s,1):
        if message=="1":
            stack.append(ind)
        elif message=="2":
            if stack:
                eliminated.add(stack.pop())
            else:
                eliminated.add(ind)
        else:
            eliminated.add(ind)
    print(len(s)-len(eliminated))
    print(*[num for num in range(1,n+1) if num not in eliminated])
            