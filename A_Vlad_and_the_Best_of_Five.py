a=int(input())
for i in range(a):
    b=input()
    c=b.count("A")
    if(c>5-c):
        print("A")
    else:
        print("B")