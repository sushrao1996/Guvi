a=float(input("Enter Physics marks : "))
b=float(input("Enter Chemistry marks : "))
c=float(input("Enter Biology marks : "))
d=float(input("Enter Mathematics marks : "))
e=float(input("Enter Computer marks : "))
Percentage=((a+b+c+d+e)/500)*100
if Percentage >=90:
    print("Grade A")
elif Percentage >=80:
    print("Grade B")
elif Percentage >=70:
    print("Grade C")
elif Percentage >=60:
    print("Grade D")
elif Percentage >=40:
    print("Grade E")
else:
    print("Grade F")
