import math 
a,b,c=map(int,input().split())
num1=math.ceil(a/c)
num2=math.ceil(b/c)
print(int(num1)*int(num2))