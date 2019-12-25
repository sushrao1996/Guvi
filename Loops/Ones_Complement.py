a=input("Enter a binary number : ")
b=[]
for i in a:
    if int(i)==0:
        b.append(1)
    elif int(i)==1:
        b.append(0)
    else:
        print("Please enter a binary number")
for i in b:
    print(i,end="")
        
