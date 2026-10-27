from collections import Counter
a=int(input())
name=input()
data=[]
for i in range(len(name)-1):
    b=name[i]+name[i+1]
    data.append(b)
out=Counter(data)
val=list(out.values())
num=max(val)
for i in  out:
    if(out[i]==num):
        print(i)
        break

