a=input("Enter a string:")
b=0
c=0
d=0
for i in a:
    if i.isalpha():
        b=b+1
    elif i.isdigit():
        c=c+1
    else:
        d=d+1
print("Number of alphabets: ",b)
print("Number of digits: ",c)
print("Number of special characters: ",d)
