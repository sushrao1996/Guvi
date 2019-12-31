a=input("Enter a string : ")
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if a==b:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")
