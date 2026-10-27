a=input()
data=[]
for i in a:
    if(i !="+"):
        data.append(i)
data.sort()
name=[]
for i in range(len(data)-1):
    name.append(data[i])
    name.append("+")
name.append(data[len(data)-1])
out="".join(a for a in name)
if("+" in a):
    print(out)
else:
    print(a)
    
    
    
    