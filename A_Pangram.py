a=int(input())
name=input()
out=name.lower()
num=set(out)
if(len(num)==26):
    print("YES")
else:
    print("NO")