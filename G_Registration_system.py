a=int(input())
dict={}
for i in range(a):
    b=input()
    if(b in dict):
        dict[b]+=1
        print(b+str(dict[b]))
    else:
        dict[b]=0
        print("OK")