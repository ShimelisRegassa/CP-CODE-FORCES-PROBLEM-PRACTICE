t=int(input())
for i in range(t):
    b=input()
    if((b[0]=="1" and int(b[1])<2) or(b[0]=="0" and int(b[1])<=9)):
        if(b[:2]=="00"):
            print("12"+b[2:]+" AM")
        else:
            print(b+" AM")
    else:
        if(int(b[:2])>12):
            val=int(b[:2])-12
            if(val>=10):
                print(str(val)+b[2:] +" PM")
            else:
                print("0"+str(val)+b[2:]+" PM")
        else:
            print(b+" PM")