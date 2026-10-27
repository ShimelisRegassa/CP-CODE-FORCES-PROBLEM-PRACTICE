t=int(input())
for i in range(t):
    l=int(input())
    b=input()
    c=input()
    na="BG"
    counter=0
    for i in range(l):
        if(b[i]==c[i] or(b[i]in na and c[i] in na)):
            counter+=1
            continue
        else:
            print("NO")
            break
    if(counter==l):
        print("YES")
            
             