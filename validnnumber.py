s=input()
power=False
digit=False
dot=False
left=0
num1="Ee"
num2="+-"
while(left<len(s)and(s[left]=="+" or s[left]=="-")):
        left+=1
while(left<len(s)):
    if(s[left].isdigit()):
        digit=True
    elif(s[left]=="."):
        if(dot  or power ):
            print(False)
            break
        dot=True
    elif(s[left] in num1):
        if(not digit or power):
            print("False")
            break
        power=True
        digit=False
    elif(s[left] in num2):
        if(s[left-1] not in num1):
            print("False")
    else:
        print("False")
        break
    left+=1
if(left==len(s)):
    print(True)
    
        
    
    