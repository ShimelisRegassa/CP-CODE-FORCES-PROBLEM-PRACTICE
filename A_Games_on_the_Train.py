import sys

data = sys.stdin.read().split()
t = int(data[0])
idx = 1
for _ in range(t):
    n = int(data[idx])
    h = [int(x) for x in data[idx+1:idx+1+n]]
    idx += n + 1
    print(max(h) - min(h) + 1)