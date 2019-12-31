a=input("Enter a string: ")
for i in range(0,len(a)):
    if a[i]!=" ":
        c=i
        break
a=a[c:]
for i in range(len(a)-1,-1,-1):
    if a[i]!=" ":
        d=i
        break
print(a[:d+1])
