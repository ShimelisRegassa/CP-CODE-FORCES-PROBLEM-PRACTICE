num=input().split()
a=int(num[0])
b=int(num[1])
data=[]
counter=0
for i in range(a):
    v=input()
    data.append(v)
check=set()
for i in range(a):
    for j in range(b):
        if(i==0):
            if(data[0][j]==num[2]):
                if(data[1][j]!="." and data[1][j]!=num[2]):
                    check.add(data[1][j])
        else:
            if(data[i][j]==num[2]):
                if(data[i-1][j]!="." and data[i-1][j]!=num[2]):
                        check.add(data[i-1][j])
                if(i+1<a and data[i+1][j]!="." and data[i+1][j]!=num[2]):
                        check.add(data[i+1][j])
print(len(check))
                    