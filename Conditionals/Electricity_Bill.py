a=int(input("Enter the number of units : "))
if a<=50:
    charge=a*0.50
elif a>50 and a<=150:
    charge=50*0.50
    a=a-50
    charge+=a*0.75
elif a>150 and a<=250:
    charge=(50*0.50)+(100*0.75)
    a=a-50-100
    charge+=a*1.20
else:
    charge=(50*0.50)+(100*0.75)+(100*1.20)
    a=a-50-100-100
    charge+=a*1.50
charge=charge+(0.2*charge)
print("Total Electricity Bill : " + str(charge))
