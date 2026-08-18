t=int(input())
for i in range(t):
    b=int(input())
    pro=input()
    fir=set()
    counter=0
    for i in pro:
        if i in fir:
            counter+=(1)
        else:
            counter+=2
            fir.add(i)
    print(counter)