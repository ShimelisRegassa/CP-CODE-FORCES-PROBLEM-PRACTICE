a=int(input())
data=list(map(int,input().split()))
num1=[]
num2=[]
num3=[]
for i in range(len(data)):
    if(data[i]==1):
        num1.append(i+1)
    elif(data[i]==2):
        num2.append(i+1)
    else:
        num3.append(i+1)
team=min(len(num1),len(num2),len(num3))
print(team)
for i in range (team):
    print(num1[i],num2[i],num3[i])
        