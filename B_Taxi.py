t = int(input())
data = list(map(int, input().split()))
counter = 0
x = data.count(1)
y = data.count(2)
z = data.count(3)
counter += data.count(4)
val=min(x, z)
counter += val
x -= val
z -= val
counter += (z)
counter += (y // 2)
y %= 2
if y > 0:
    counter += 1
    x = max(0, x -min(x,2))
if(x>0):
    counter += ((x + 3) // 4)
print(counter)