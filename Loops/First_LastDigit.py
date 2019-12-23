a=input("Enter a Number : ")
for i in range(len(a)):
    if (i==0):
        print(a[i] + " is the first digit")
    elif(i==len(a)-1):
        print(a[i] + " is the last digit")

