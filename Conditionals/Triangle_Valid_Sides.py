a=float(input("Enter length of side1 : "))
b=float(input("Enter length of side2 : "))
c=float(input("Enter length of side3 : "))
if ((a+b)>c) and ((b+c)>a) and ((a+c)>b) :
    print("Triangle is Valid.")
else:
    print("Triangle is not Valid.")
