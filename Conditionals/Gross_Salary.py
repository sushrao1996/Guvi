BS=float(input("Enter Basic Salary : "))
if BS <=10000:
    HRA=BS*0.2
    DA=BS*0.8
elif BS <=20000:
    HRA=BS*0.25
    DA=BS*0.9
else:
    HRA=BS*0.3
    DA=BS*0.95
GS=BS+HRA+DA
print("Gross Salary : " + str(GS))
