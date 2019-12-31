a=input("Enter a string : ")
b=input("Enter a character whose all occurence has to be found : ")
l=[]
for i in range(len(a)):
    if b==a[i]:
        l.append(i+1)
print("The character is found at the below positions: ",l)
