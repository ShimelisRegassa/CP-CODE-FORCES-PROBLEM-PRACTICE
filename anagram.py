from collections import Counter
word1=input()
word2=input()
left=0
num=Counter(word2)
counter=0
while(left<len(word1)-len(word2)+1):
      num1=word1[left:left+len(word2)]
      if(Counter(num1)==num):
          counter+=1
      left+=1
print(counter)
