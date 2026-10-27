s=input()
d=s.upper()
e=s[0].lower()+s[1:].upper()
if(s==d or s==e):
    if(s==d):
        print(s.lower())
    else:
        print(s[0].upper()+s[1:].lower())
else:
    print(s)