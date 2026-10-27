a=int(input())
name=input()
ans=0
current=0
for i in range(len(name)):
    if(name[i]=="x"):
        current+=1
    else:
        current=0
    if(current>2):
        ans+=1
print(ans)
