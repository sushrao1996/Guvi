def diameter_func(r):
    d=2*r
    return d
def circum_func(r):
    c=2*3.14*r
    return c
def area_func(r):
    a=3.14*r*r
    return a
r1=float(input("Enter the radius : "))
diameter=diameter_func(r1)
print("Diameter of the Circle : ",diameter)
circumference=circum_func(r1)
print("Circumference of the Circle : ",round(circumference,2))
area=area_func(r1)
print("Area of the Circle : ",area)
