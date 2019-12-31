a=input("Enter a string: ")
b=input("Enter the word whose first occurrence in the string has to be found: ")
d=a.split(" ")
for i in range(0,len(d)):
    if b==d[i]:
        print("First occurence of the word is at position : ",i+1)
        break


         
