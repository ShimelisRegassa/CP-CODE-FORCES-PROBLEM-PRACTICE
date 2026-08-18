a = int(input())
counter = 0
for i in range(6,a+1):
    tem=0
    m=2
    while(m*m<=i):
        if(i%m==0):
            tem+=1
        while(i%m==0):
            i//=m
        m+=1
    if(i>1):
        tem+=1
    if(tem==2):
        counter+=1
print(counter)