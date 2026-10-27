n=int(input())
num1=list(map(int,input().split()))
m=int(input())
num2=list(map(int,input().split()))
num1.sort()
num2.sort()
right=0
counter=0
left=0
while(left<len(num1) and right<len(num2)):
    if(abs(num1[left]-num2[right])<=1):
        right+=1
        left+=1
        counter+=1
    elif(num1[left]>num2[right]):
        right+=1
    else:
        left+=1
print(counter)
\


            
    