num=input()
data=input().split()
for i in data:
    if(i[0] in num or i[1] in num):
        print("YES")
        break
else:
    print("NO")