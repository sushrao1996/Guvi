l=[]
for i in range(2000,3201):
        if i%7==0 and i%5!=0:
            l.append(i)
for i in range(len(l)):
    if i!=len(l)-1:
        print(l[i],end=",")
    else:
        print(l[i],end=".")
    
