s=input()
k=int(input())
b=len(s)
counter=0
for i in range(b):
    m=k
    right=i
    ans={s[i]}
    add=0
    while(right<b):
        if(s[right]not in ans):
            if(m>0):
                add+=1
                m-=1
            else:
                break
        else:
            add+=1
        right+=1
    counter=max(counter,add)
print(counter)
