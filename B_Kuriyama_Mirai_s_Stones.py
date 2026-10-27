n=int(input())
data=list(map(int,input().split()))
m=int(input())
num=sorted(data)
arra1=[0]*len(data)
arra2=[0]*len(data)
val1=0
val2=0
for i in range(len(data)):
    val1+=data[i]
    val2+=num[i]
    arra1[i]=val1
    arra2[i]=val2    
for i in range(m):
    t,l,r=map(int,input().split())
    if(t==1):
        if(l==1):
            print(arra1[r-1])
        else:
            print(arra1[r-1]-arra1[l-2])
    else:
        if(l==1):
            print(arra2[r-1])
        else:
            print(arra2[r-1]-arra2[l-2])
    
    
    