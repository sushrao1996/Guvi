a=input("Enter a Number : ")
b=0
d=0
c=[]
for i in range(len(a)):
    if (i==0):
        b=a[i]
    elif(i==len(a)-1):
        d=a[i]
    else:
        c.append(a[i])
e=[]
e.append(int(d))
for i in c:
    e.append(int(i))
e.append(int(b))
for i in e:
    print(i,end="")
    
        

