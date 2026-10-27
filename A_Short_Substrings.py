a=int(input())
for i in range(a):
    b=input()
    name=""
    for i in range(len(b)-1):
        if(i%2==0):
            name+=b[i]
    name+=b[len(b)-1]
    print(name)
            
    