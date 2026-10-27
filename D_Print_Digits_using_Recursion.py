n=int(input())
for i in range(n):
    b=input()
    m=0
    def recursion(m):
        if(m==len(b)):
            return 
        if(m==len(b)-1):
            print(b[m])
        else:
            print(b[m],end=" ")
        m+=1
        recursion(m)
    recursion(m)