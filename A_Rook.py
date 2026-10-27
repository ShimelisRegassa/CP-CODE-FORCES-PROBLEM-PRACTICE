a=int(input())
for i in range(a):
    b=input()
    data=[]
    data1=["a","b","c","d","e","f","g","h"]
    for i in range(1,9):
        if(i!=int(b[1])):
            data.append(b[0]+str(i))
    for i in data1:
        if(i!=b[0]):
            data.append(i+b[1])
    for i in data:
        print(i)
    