a=input("Enter a string :")
b=""
for i in a:
    if i>='a' and i<='z':
        b=b+chr(ord(i)-32)
    elif i>='A' and i<='Z':
        b=b+chr(ord(i)+32)
    else:
        b=b+i
print("Before Toggling : ",a)
print("After Toggling : ",b)
