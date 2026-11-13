t=int(input())
for i in range(t):
    n=int(input())
    val1=""
    val2=""
    for i in range(n):
        if(i%2==0):
            val1+="##"
        else:
            val1+=".."
    for i in range(n):
        if(i%2==0):
            val2+=".."
        else:
            val2+="##"
    fin=[]
    for i in range(n):
        if(i%2==0):
            fin.append(val1)
            fin.append(val1)
        else:
            fin.append(val2)
            fin.append(val2)
    for i in fin:
        print(i)
            
            
    
                
    
