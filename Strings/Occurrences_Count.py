a=input("Enter a string : ")
b=input("Enter a character whose count of occurence has to be found : ")
c=0
for i in range(len(a)):
    if b==a[i]:
        c+=1
print("Occurrences count: ",c)
