n=int(input())
s=input()
ch=set(s)
num={}
right=0
left=0
counter=float("inf")
while(right<n):
    num[s[right]]=num.get(s[right],0)+1
    while(len(num)==len(ch)):
        counter=min(counter,right-left+1)
        num[s[left]]-=1
        if(num[s[left]]==0):
            del num[s[left]]
        left+=1
    right+=1
print(counter)