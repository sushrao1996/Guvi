a=input("Enter a number : ")
b=input("Enter a digit whose frequency has to be checked : ")
c=0
for i in a:
    if b==i:
        c+=1
print(b + " is present " + str(c) + " times in " + a)
