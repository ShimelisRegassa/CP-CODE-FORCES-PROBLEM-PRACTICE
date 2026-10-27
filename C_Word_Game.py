t=int(input())
for i in range(t):
    b=int(input())
    nums1=set(input().split())
    nums2=set(input().split())
    nums3=set(input().split())
    ob={}
    point1=0
    point2=0
    point3=0
    for i in nums1:
        ob[i]=ob.get(i,0)+1
    for i in nums2:
        ob[i]=ob.get(i,0)+1
    for i in nums3:
        ob[i]=ob.get(i,0)+1
    for i in ob:
        if(ob[i]==1):
            if(i in nums1):
                point1+=3
            elif(i in nums2):
                point2+=3
            else:
                point3+=3
           
        elif(ob[i]==2):
            if(i in nums1 and i in nums2):
                point1+=1
                point2+=1
            elif(i in nums2 and i in nums3):
                point2+=1
                point3+=1
            elif(i in nums1 and i in nums3):
                point1+=1
                point3+=1
    print(point1,point2,point3)
            
            
            
    
    
    

                
    
            
        
        
        
    