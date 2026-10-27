from collections import Counter
s=input()
ob=Counter(s)
num=list(ob.most_common())
res=""
for i in num:
    res+=(i[0]*i[1])
print(res)
