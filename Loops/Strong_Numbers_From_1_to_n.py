j=input("Enter a number : ")
e=[]
for a in range(1,int(j)+1):
    c=[]
    for i in str(a):
        b=1
        for j in range(1,int(i)+1):
            b=b*j
        c.append(b)
    d=0
    for i in c:
        d+=i
    if d==int(a):
        e.append(int(a))
print(e)
   
