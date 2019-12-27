a=input("Enter a Character : ")
b=[]
for i in range(0,10):
    b.append(str(i))
if (a>'a' and a<'z') or (a>'A' and a<'Z'):
     print("The character entered in an alphabet")
elif a in b:
     print("The character entered in a digit")
else:
     print("The character entered in a special character")
