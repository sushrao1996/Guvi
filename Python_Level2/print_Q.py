C=50
H=30
n=input("Enter the values of D : ")
D=n.split(",")
for i in range(len(D)):
    Q=((2*C*int(D[i]))/H)**0.5
    if i!=len(D)-1:
        print(round(Q),end=",")
    else:
        print(round(Q),end="")
        
