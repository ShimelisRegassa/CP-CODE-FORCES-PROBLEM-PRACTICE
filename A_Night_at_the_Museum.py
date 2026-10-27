n=input()
ob={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"n":15,"o":16,"p":16,"q":17,
    "r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
total=0
num=ob[n[0]]-ob["a"]
total=min(abs(num),26-abs(num))
for i in range(len(n)-1):
    m=abs(ob[n[i]]-ob[n[i+1]])
    total+=min(m,26-m)
print(total)