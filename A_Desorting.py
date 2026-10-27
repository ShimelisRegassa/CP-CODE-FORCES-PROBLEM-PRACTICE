a=int(input())
for i in range(a):
    n=int(input())
    min_ops = float('inf')
    already_not_sorted = False

    for j in range(n - 1):
        diff = a[j + 1] - a[j]
    if diff < 0:
        already_not_sorted = True
        break
    ops = (diff // 2) + 1
    if ops < min_ops:
        min_ops = ops

if already_not_sorted:
    print(0)
else:
    print(min_ops)