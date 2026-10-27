n=int(input())
num=list(map(int,input().split()))
if(n%2==1):
    m=n-1
else:
    m=n-2
def recursion(m,num,n):
    if(m==0):
        print(num[m])
        return
    elif(m<0):
        return 
    print( num[m],end=" ")
    m-=2 
    recursion(m,num,n)
recursion(m,num,n)

    
    