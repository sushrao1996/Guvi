a=input("Enter a string : ")
b=input("Enter a character whose last occurence has to be found : ")
for i in range(len(a)-1,-1,-1):
    if b==a[i]:
        print("Last occurence is at position: ",i+1)
        break
