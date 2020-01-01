def max_func(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
def min_func(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2
n1=int(input("Enter number1 : "))
n2=int(input("Enter number2 : "))
if n1==n2:
    print("Both the numbers are equal.")
else:
    print("Maximum of the 2 numbers : ",max_func(n1,n2))
    print("Minimum of the 2 numbers : ",min_func(n1,n2))
    
