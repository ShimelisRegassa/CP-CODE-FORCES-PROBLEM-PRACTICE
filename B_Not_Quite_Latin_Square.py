a=int(input())
for i in range(a):
    mat=[]
    for i in range(3):
        b=input()
        mat.append(b)
    for i in range(3):
        for j in range(3):
            if(mat[i][j]=="?"):
                m="".join(mat[i])
                break
    name="ABC"
    for i in name:
        if(i not in m):
            print(i)