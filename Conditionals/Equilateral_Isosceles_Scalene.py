a=float(input("Enter length of side1 : "))
b=float(input("Enter length of side2 : "))
c=float(input("Enter length of side3 : "))
if (a==b==c):
    print("Equilateral triangle")
elif (a==b) or (b==c) or (a==c):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
