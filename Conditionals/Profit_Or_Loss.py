SP=float(input("Enter the selling price : "))
CP=float(input("Enter the cost price : "))
if SP>CP:
    print("Profit : " + str(SP-CP))
elif CP>SP:
    print("Loss : " +str(CP-SP))
else:
    print("No Profit, No Loss")
