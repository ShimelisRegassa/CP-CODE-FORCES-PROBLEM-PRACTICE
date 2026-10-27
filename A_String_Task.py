s=input()
sm="AOYEUI"
ca=sm.lower()
res=""
for i in s:
    if(i in sm or i in ca):
        continue
    else:
        res+="."
        res+=i.lower()
print(res)