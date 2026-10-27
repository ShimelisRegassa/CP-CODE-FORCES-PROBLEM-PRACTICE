s=input()
list1=["abc","def","ghi","jkl","mno","pqrs","tuv","xyz"]
num=[""]
if(len(s)==0):
    print([])
else:
    for i in s:
        ans=[]
        val=list1[int(i)-2]
        for j in num:
            for m in val:
                ans.append(j+m)
        num=ans
    print(num)
            
                
   
                