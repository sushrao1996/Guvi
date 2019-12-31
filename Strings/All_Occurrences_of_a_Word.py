a=input("Enter a string: ")
b=input("Enter the word whose first occurrence in the string has to be found: ")
d=a.split(" ")
l=[]
for i in range(0,len(d)):
    if b==d[i]:
        l.append(i+1)
print(b," is found at positions ",l)


         
