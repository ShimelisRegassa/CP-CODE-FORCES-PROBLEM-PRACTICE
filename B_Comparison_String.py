t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    counter=1
    res=1
    for j in range(len(s)-1):
        if(s[j]==s[j+1]):
            counter+=1
        else:
            counter=1
        res=max(res,counter)
    
    print(max(res,counter)+1)
    