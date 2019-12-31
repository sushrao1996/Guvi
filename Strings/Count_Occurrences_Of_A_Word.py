a=input("Enter a string: ")
b=input("Enter the word whose count of occurrence in the string has to be found: ")
d=a.split(" ")
c=0
for i in range(0,len(d)):
    if b==d[i]:
        c+=1
print(b," is found ",c," times.")
