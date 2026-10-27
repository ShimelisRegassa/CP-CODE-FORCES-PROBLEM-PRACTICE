n, m = map(int, input().split())
if m<=n:
    print(n-m)
else:
    counter = 0
    while m>n:
        if m%2==0:
            m = m//2
            counter += 1
        else:
            m += 1
            counter += 1
    counter += n-m
    print(counter)
            