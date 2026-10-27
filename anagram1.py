s=input()
p=input()
a=len(s)
b=len(p)
fir=[0]*26
sec=[0]*26
num=[]
for i in p:
    fir[ord(i)-97]+=1
for i in s[:b]:
    sec[ord(i)-97]+=1

if(fir==sec):
    print([0])
else:
    c=b
    for i in range(c,a):
        sec[ord(s[i])-97]+=1
        sec[ord(s[i]-c)-97]-=1
        if(fir==sec):
            num.append(i-b+1)
    print(num)
    
        
    
