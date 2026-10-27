a,b=map(int,input().split())
counter=0
n=a
while(a>=b):
    counter+=(a//b)
    a=(a//b)+a%b
print(n+counter)
    
    
