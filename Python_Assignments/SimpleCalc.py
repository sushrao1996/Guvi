def input1():
    num1=input("Enter number1 : ")
    try:
       val = int(num1)
       return val
    except ValueError:
      try:
        val = float(num1)
        return val
      except ValueError:
          print("Input is not a number. It's a string.Please enter a valid number.")
          input1()
num1=input1()
num1=float(num1)
def input2():
    num2=input("Enter number2 : ")
    try:
       val = int(num2)
       return val
    except ValueError:
      try:
        val = float(num2)
        return val
      except ValueError:
          print("Input is not a number. It's a string.Please enter a valid number.")
          input2()     
num2=input2()
num2=float(num2)
def calculater():
    dict={1:"ADD",2:"SUB",3:"MUL",4:"DIV",5:"MOD"}
    for i,j in dict.items():
        print(i,":",j)
    a=int(input("Enter the operation number :"))
    if a not in dict.keys():
        print("Enter a valid operation number.")
        calculater()
    else:
        if a==1:
            add=num1+num2
            print(add)
        elif a==2:
            sub=num1-num2
            print(sub)
        elif a==3:
            mul=num1*num2
            print(mul)
        elif a==4:
            div=num1/num2
            print(div)
        else:
            mod=num1%num2
            print(mod)
calculater()
        
