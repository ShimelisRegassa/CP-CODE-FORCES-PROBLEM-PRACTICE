s,n=map(int,input().split())
data=[]
for i in range(n):
    a,b=map(int,input().split())
    data.append((a,b))
data.sort(key=lambda x:x[0])
power=s
counter=0
for i in data:
    if(power>i[0]):
        counter+=1
        power+=i[1]
    else:
        print("NO")
        break
if(counter==n):
    print("YES")
    