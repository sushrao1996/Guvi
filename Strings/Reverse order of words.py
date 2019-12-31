a=input("Enter a string: ")
d=a.split(" ")
l=[]
for i in range(len(d)-1,-1,-1):
    l.append(d[i])
c=""
for i in l:
    c+=i+" "
print(c)
