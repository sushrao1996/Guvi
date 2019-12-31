a=input("Enter a string : ")
b=a.split(" ")
c=""
l=[]
for i in b:
    if i!=c:
        l.append(i)
d=""
for i in l:
    d=d+i+" "
print(d)
    
