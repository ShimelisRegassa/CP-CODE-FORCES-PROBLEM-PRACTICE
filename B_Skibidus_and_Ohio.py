a=int(input())
for i in range(a):
    name=input()
    for i in range(len(name)-1):
        if(name[i]==name[i+1]):
            print(1)
            break
    else:
        print(len(name))  
            