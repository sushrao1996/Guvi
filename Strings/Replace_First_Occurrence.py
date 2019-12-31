a=input("Enter a string : ")
b=input("Enter a character whose first occurence has to be replaced : ")
for i in range(len(a)):
    if b==a[i]:
        c=i
        break
print(a[:c]+"*"+a[c+1:])
