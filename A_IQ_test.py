n=int(input())
num=list(map(int,input().split()))
counter1=[]
counter2=[]
for i in  range(n):
    if(num[i]%2==0):
        counter1.append(i)
    else:
        counter2.append(i)
if(len(counter1)==1):
    print(counter1[0]+1)
else:
    print(counter2[0]+1)