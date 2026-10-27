a=input()
b=int(a)+1
while(b>int(a)):
      num=set(str(b))
      if(len(num)==4):
          break
      b+=1
    
print(b)