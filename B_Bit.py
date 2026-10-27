a=int(input())
count=0
for i in range(a):
    b=input()
    if(b=="++X" or b=="X++"):
        count+=1
    else:
        count-=1
print(count)