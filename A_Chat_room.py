word=input()
num="hello"
i=0
name=""
for j in word:
    if(j==num[i]):
        name+=j
        i+=1
    if(name==num):
        print("YES")
        break
else:
    print("NO")
    

