a=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
total=sum(data)
count=0
summation=0
for i in range(len(data)):
    summation+=data[i]
    if(summation>total-summation):
        count+=1
        break
    else:
        count+=1
print(count)
    
