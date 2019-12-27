a=['january','march','may','july','august','october','december']
b=['february']
c=['april','june','september','november']
d=input("Enter Month Name : ")
d=d.lower()
if d in a:
    print(d + " has 31 days.")
elif d in b:
    print(d + " has 28 or 29 days based on leap year.")
elif d in c:
    print(d + " has 30 days.")
else:
    print("Enter a valid month name.")
