a, b, c, d = map(int, input().split())
n = a
x, y, z = b, c, d
res = 0
for i in range(n // x + 1):
    for j in range((n - i * x) // y + 1):
        rem = n - (i * x + j * y)
        if rem % z == 0:
            k = rem // z
            if i + j + k > res:
                res = i + j + k
print(res)