a=input("Enter the length in Centimeters : ")

#Converting into meters
#1cm=0.001m

LenInMeters=int(a)*0.001
print("Length in meters : " + str(LenInMeters))

#Conversion into kilometers
#1cm=1*10^(-5)km

LenInKilometers=int(a)/100000
print("Length in Kilometers : " + str(LenInKilometers))
