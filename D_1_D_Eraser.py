a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    name=input()
    i=0
    counter=0
    while(i<len(name)):
        if(name[i]=="B"):
            counter+=1
            i+=c
        else:
            i+=1
    print(counter)