a=input("Enter a string: ")
b=input("Enter the word whose last occurrence in the string has to be found: ")
d=a.split(" ")
for i in range(len(d)-1,-1,-1):
    if b==d[i]:
        print("Last occurence of the word is at position : ",i+1)
        break


         
