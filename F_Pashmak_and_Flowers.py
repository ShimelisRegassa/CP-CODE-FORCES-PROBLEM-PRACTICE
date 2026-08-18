n=int(input())
b=list(map(int,input().split()))
great=max(b)
less=min(b)

if great==less:
    print(0,((n)*(n-1)//2))
else:
    nogreat=b.count(great)
    noless=b.count(less)
    
    print(great-less,nogreat*noless)