a=int(input())
database={}
for i in range(a):
    name=input()
    if name in database:
        database[name]+=1
        print(name+str(database[name]))
    else:
        print("OK")
        database[name]=0