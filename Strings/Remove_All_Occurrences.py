a=input("Enter a string : ")
b=input("Enter a character whose occurences has to be removed : ")
c=""
for i in range(0,len(a)):
    if b==a[i]:
        c+=""
    else:
        c+=a[i]
print(c)
