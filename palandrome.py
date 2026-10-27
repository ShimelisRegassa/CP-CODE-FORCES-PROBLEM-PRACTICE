s=input()
long=0
num=[]
for i in range(len(s)-1):
    left=i+1
    while(left<len(s)):
        b=s[i:left+1]
        c= b[::-1]
        if(c==b):
            long=max(long,len(c))
            num.append(c)
        left+=1
for i in num:
    if(len(i)==long):
        print(i)
        break
