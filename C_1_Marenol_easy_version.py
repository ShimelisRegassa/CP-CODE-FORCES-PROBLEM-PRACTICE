t=int(input())
for i in range(t):
    b=int(input())
    s=input()
    r=input()
    if(b<3):
        if(s==r):
            print("YES")
        else:
            print("NO")
    else:
        if(s.count("0")!=r.count("0")):
            print("NO")
        else:
            sum1=0
            sum2=0
            for j in range(b):
                if(s[j]=="1"):
                    sum1+=j
                if(r[j]=="1"):
                    sum2+=j
            if(sum1%2 ==sum2%2):
                print("YES")
            else:
                print("NO")
