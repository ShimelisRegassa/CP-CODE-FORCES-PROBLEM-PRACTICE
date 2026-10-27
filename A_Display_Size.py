import math
a=int(input())
for b in range(int(math.sqrt(a)),0,-1):
    if(a%b==0):
        c=a//b
        print(a//c,c)
        break
