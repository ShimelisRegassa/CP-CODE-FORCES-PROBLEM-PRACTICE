a=int(input())
for i in range(a):
    b=input()
    c=input()
    dis=0
    for i in range(len(c)-1):
        dis+=abs(b.index(c[i+1])-b.index(c[i]))
    print(dis)   