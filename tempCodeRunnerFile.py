t=int(input())
for i in range(t):
    b=int(input())
    val="a"
    s=input()
    for i in s:
        if(i>val):
            val=i
    print(ord(val)-ord("a")+1)
    