a=int(input())
for i in range(a):
    data=[]
    for i in range(10):
        row=input()
        data.append(row)
    counter=0
    for i in range(10):
        for j in range(10):
            if(data[i][j]=="X"):
                num=min(i+1,j+1,10-i,10-j)
                counter+=num
    print(counter)