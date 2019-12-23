a=input("Enter a Number : ")
b=0
for i in range(len(a)):
    if (i==0):
        b+=int(a[i])
    elif(i==len(a)-1):
        b+=int(a[i])
print("Sum of First and Last Digit is " + str(b))

