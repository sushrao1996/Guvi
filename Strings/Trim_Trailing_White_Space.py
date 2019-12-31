a=input("Enter a string: ")
for i in range(len(a)-1,-1,-1):
    if a[i]!=" ":
        c=i
        break
print(a[:c+1])
