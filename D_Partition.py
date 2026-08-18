a=int(input())
data=list(map(int,input().split()))
num1=[]
num2=[]
for i in data:
    if(i<0):
        num2.append(i)
    else:
        num1.append(i)
sum1=sum(num1)
sum2=sum(num2)
print(sum1-sum2)
