a=int(input("Enter number1 : "))
b=int(input("Enter number2 : "))
c=int(input("Enter number3 : "))
if a>b:
    if a>c:
        print("Number1 is the greatest")
    else:
        print("Number3 is the greatest")
elif b>c:
    print("Number 2 is greatest")
else:
    print("Number3 is greatest")
