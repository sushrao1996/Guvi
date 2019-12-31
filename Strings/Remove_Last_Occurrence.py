a=input("Enter a string : ")
b=input("Enter a character whose last occurence has to be removed : ")
for i in range(len(a)-1,-1,-1):
    if b==a[i]:
        c=i
        break
print(a[:c]+a[c+1:])
