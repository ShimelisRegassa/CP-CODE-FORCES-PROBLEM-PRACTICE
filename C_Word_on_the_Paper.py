t=int(input())
for i in range(t):
    res=[]
    for i in range(8):
        row=input()
        res.append(row)
    val=""
    for i in range(8):
        for j in range(8):
            if(res[i][j]!="."):
                val+=res[i][j]
    print(val)