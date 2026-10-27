n=int(input())
m=1
def recursion(m,n):
    if(m>n):
        return 
    val=2*m-1
    print(" "*(n-m)+"*"*val)
    recursion(m+1,n)
recursion(m,n)
    
 