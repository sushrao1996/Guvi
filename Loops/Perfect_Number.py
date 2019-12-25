a=input("Enter a number : ")
b=[]
for i in range(0,int(a)+1):
    for j in range(0,int(a)+1):
        if int(i)*int(j)==int(a):
            b.append(i)
b.pop(-1)
c=0
for i in b:
    c+=int(i)
if c==int(a):
    print(str(a) + " is a perfect number")
else:
    print(str(a) + " is not a perfect number")


