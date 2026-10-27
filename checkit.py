t=int(input())
for i in range(t):
    b=int(input())
    num=input()
    data=[num[0]]
    counter=1
    for i in range(1,b-1):
        if(num[i] in data):
            print("Yes")
            break
        else:
            data.append(num[i])
        counter+=1
        if(counter==b-1):
            if(num[i]==num[b-1]):
                print("Yes")
                break
    else:
        print("No")
            
 
 