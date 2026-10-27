a=int(input())
data=list(map(int,input().split()))
left=0
maximum=0
fir=0
sec=0
while(left<a-2):
    sum=data[left]+data[left+1]+data[left+2]
    if(sum>maximum):
        maximum=sum
        fir=left
        sec=left+1
        thr=left+2
    left+=1
print(f"maximum sum is :{maximum} ,at index {fir} , {sec} and {thr}")