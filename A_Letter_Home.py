t=int(input())
for i in range(t):
    c,b=map(int,input().split())
    num=list(map(int,input().split()))
    great=max(num)
    small=min(num)
    if(small<b and b<great):
        if((b-small)<=(great-b)):
            print(2*(b-small)+(great-b))
        else:
            print(2*(great-b)+(b-small))
    elif(b>=great):
        print(b-small)
    else:
        print(great-b)
