a=input("Enter a string: ")
for i in range(0,len(a)):
    if a[i]!=" ":
        c=i
        break
print(a[c:])
