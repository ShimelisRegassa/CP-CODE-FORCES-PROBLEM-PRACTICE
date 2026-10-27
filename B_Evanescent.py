t = int(input())
for _ in range(t):
    b = int(input())
    s = input()
    fir= 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            fir += 1    
    res= fir
    for i in range(1, len(s) - 1):
        left, mid, right = s[i-1], s[i], s[i+1]
        if left == mid:
            if(right==mid):
                old=1
            else:
                old=2
        
        else:
            if(right!=mid):
                old=3
            else:
                old=2 
        if(left==right):
            new=1
        else:
            new=2
        
        reduction = old - new
        if reduction > 0:
            current = fir - reduction
            if current < res:
                res= current      
    print(res)
        
    