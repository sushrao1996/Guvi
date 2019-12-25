a=input("Enter a number : ")
b=[]
for i in range(0,int(a)+1):
    for j in range(0,int(a)+1):
        if int(i)*int(j)==int(a):
            b.append(i)
            b.append(j)
print(b)
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(c)
