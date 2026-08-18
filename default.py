a=int(input())
data=list(map(int,input().split()))
b=int(input())
lst=list(map(int,input().split()))
fir=0
sec=0
num=[]
while(fir<len(data) and sec<len(lst)):
    if(data[fir]<lst[sec]):
        num.append(data[fir])
        fir+=1
    else:
        num.append(lst[sec])
        sec+=1
while(fir<len(data)):
    num.append(data[fir])
    fir+=1
while(sec<len(lst)):
    num.append(lst[sec])
    sec+=1
print(*num)
        