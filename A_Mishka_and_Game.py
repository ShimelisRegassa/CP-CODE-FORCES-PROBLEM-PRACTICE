a=int(input())
count1=0
count2=0
for i in range(a):
    b,c=map(int,input().split())
    if(b>c):
        count1+=1
    elif(c>b):
        count2+=1
if(count1>count2):
    print("Mishka")
elif(count1<count2):
    print("Chris")
else:
    print("Friendship is magic!^^")
    