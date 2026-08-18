from collections import Counter
t=int(input())
for i in range(t):
    b=int(input())
    data=input().split()
    num="01032025"
    val=Counter(num)
    dic=Counter()
    counter=0
    for i in data:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
        bool=True
        for char in num:
            if(dic[char]<val[char]):
                counter+=1
                bool=False
                break
        if(bool):
            print(counter+1)
            break  
    else:
        print(0)
    
    


    