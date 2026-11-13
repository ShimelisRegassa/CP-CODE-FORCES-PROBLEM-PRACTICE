t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=input()
    counter=0
    if s[:b].count("0")==0:
        counter+=1
    for i in range(b,a-b+1,b):
        if(s[i:b+i].count("0")==0):
            counter+=1
    print(counter)
        