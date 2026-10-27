name=input()
left=0
right=0
num=[]
long=0
add=0
while(right<len(name) and left<len(name)):
    if(name[right] not in num):
        num.append(name[right])
        add+=1
        right+=1
    else:
        num.clear()
        left+=1
        add=0
        right=left
    if(add>long):
        long=add
print(long)