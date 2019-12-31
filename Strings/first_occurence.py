a=input("Enter a string : ")
b=input("Enter a character whose first occurence has to be found : ")
for i in range(len(a)):
    if b==a[i]:
        print("First occurence is at position: ",i+1)
        break
