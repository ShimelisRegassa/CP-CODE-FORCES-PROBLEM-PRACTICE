s=input()
ob={}
for i in range(len(s)):
    ob[s[i]]=i
start=0
end=0
res=[]
for i in range(len(s)):
    end=max(end,ob[s[i]])
    if(i==end):
        res.append(i-start+1)
        start=i+1
print(res)