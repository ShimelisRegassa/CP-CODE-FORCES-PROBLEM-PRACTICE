n=int(input())
val=1
def recursion(val):
    if(val==n+1):
        return 
    print(val)
    val+=1
    recursion(val)
recursion(val)
    