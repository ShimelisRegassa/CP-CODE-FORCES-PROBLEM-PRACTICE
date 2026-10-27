a=int(input())
for i in range(a):
    n=int(input())
    data=input().split()
    num1=data.count("1")
    num2=data.count("-1")
    counter=0
    while(num1<num2):
        num1+=1
        num2-=1
        counter+=1
    if(num2%2==1):
        counter+=1
    print(counter)
        