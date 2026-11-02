t=int(input())
for i in range(t):
    s=input()
    val=""
    cap=[]
    sma=[]
    for i in s:
        if(i =="b" or i=="B"):
            if(i=="b" and len(val)!=0 ):
                val=val[:len(val)-1]
            if(i=="B" and len(val)!=0 and val[-1]==val[-1].upper()):
                val=val[:len(val)-1]
        else:
            val+=i
    print(val)
    