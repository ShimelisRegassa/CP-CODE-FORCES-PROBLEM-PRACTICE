data=list(map(int,input().split()))
name=[]
for  i  in data:
    if(i not in name):
        name.append(i)
print(4-len(name))