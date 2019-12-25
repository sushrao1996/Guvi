a=input("Enter a number : ")
c=[]
for i in a:
    b=1
    for j in range(1,int(i)+1):
        b=b*j
    c.append(b)
d=0
for i in c:
    d+=i
if d==int(a):
    print(str(a) + " is a strong number.")
else:
    print(str(a) + " is not a strong number.")
        
