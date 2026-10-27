import math
from collections import defaultdict
lis= [2,3,4,2,4,7,2]
dict=defaultdict(int)
for i in lis:
    dict[i]+=1
print(dict)
print(all(lis))
print(any(lis))
print(chr(65))
print(ord("h"))
ov=("banana"+"eating")
print(type(ov))
fun=lambda x:x**2
out=map(fun,lis)
print(list(out))
data=[1,2,3,4,5,6,7]
fun2=lambda x:x%2
data1=[4,5,6,7,8,9,9]
out=list(filter(fun2,data))
num2="0,1,2,3,4,5,6"
print(num2.split(","))
print(out)
num=list(zip(data,lis,data1))
print(num)
print(math.pow(3,4))
print(math.prod(data1))
second="   Hello everyone in the class\t\n "
sec=second.strip()
print(sec)
final="hello everyone in the class ,are you oky !"
sec1=final.replace("hello","Hello")
print(f"{final},{sec1}")