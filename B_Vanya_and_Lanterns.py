a,b=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
distance=data[0]
for i in range(len(data)-1):
    dis=data[i+1]-data[i]
    dis/=2
    distance=max(distance,dis)
distance=max(b-data[len(data)-1],distance)
print(f"{distance:.10f}")
