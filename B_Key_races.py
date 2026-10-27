a,b,c,d,e =(map(int,input().split()))
fir=a*b+(2*d)
sec=a*c+(2*e)
if(fir<sec):
    print("First")
elif(fir>sec):
    print("Second")
else:
    print("Friendship")
