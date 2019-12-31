a=input("Enter a string : ")
b=input("Enter a word whose last occurence has to be removed : ")
d=a.split(" ")
c=""
for i in range(len(d)):
    if b==d[i]:
        c+=""
    else:
        c+=d[i]+" "
print(c)
