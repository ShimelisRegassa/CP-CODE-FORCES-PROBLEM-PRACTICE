t=int(input())
for i in range(t):
    n=int(input())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    counter=0
    for i in range(n-1):
        if num1[i]>num2[i+1]:
            counter+=(num1[i]-num2[i+1])
    print(counter+num1[n-1])
            
    