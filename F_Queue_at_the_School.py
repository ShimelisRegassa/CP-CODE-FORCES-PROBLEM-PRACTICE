a,b=map(int,input().split())
arra=input()
num=list(arra)
for i in range(b):
    left=0
    while(left<len(arra)-1):
        if(num[left]=="B" and num[left+1]=="G"):
            num[left],num[left+1]=num[left+1],num[left]
            left+=2
        else:
            left+=1
print("".join(num))
        
    
        
    
            
