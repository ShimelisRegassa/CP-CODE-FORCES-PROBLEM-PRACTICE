data=list(map(int,input().split()))
a=input()
count=0
for i in a:
    count+=data[int(i)-1]
print(count)
    

