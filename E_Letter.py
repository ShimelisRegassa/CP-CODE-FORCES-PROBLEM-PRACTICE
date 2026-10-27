from collections import Counter

s1=Counter("".join(input().split()))
s2=Counter("".join(input().split()))
for key in s2:
    if s2[key]>s1[key]:
        print("NO")
        break   
else:
    print("YES")