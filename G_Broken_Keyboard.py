a=int(input())
for i in range(a):
    b=input()
    if(len(b)==1):
        print(b)
    else:
        i=0
        name=""
        while(i<len(b)-1):
            if(b[i]==b[i+1]):
                i+=2
            else:
                if b[i] not in name:
                    name+=b[i]
                i+=1
        
        if i==len(b)-1:
            if b[i] not in name:
                name+=b[i]
                

        print("".join(sorted(name)))
                
    