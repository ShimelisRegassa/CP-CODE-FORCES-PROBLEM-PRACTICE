n=int(input())
num=list(map(int,input().split()))
data=sorted(num)
k=int(input())
num1=[0]*len(num)
num1[0]=num[0]
data1=[0]*len(num)
data1[0]=data[0]
for j in range(1,len(num)):
    num1[j]=num1[j-1]+num[j]
    data1[j]=data1[j-1]+data[j]
for j in range(k):
    a,b,c=map(int,input().split())
    b,c=b-1,c-1
    if(a==1):
        if(b!=0):
            print(num1[c]-num1[b-1])
        else:
            print(num1[c])
    else:
        if(b!=0):
            print(data1[c]-data1[b-1])
        else:
            print(data1[c])
            
    