a=input("Enter the number of rows: ")
b=65
for i in range(1,int(a)+1):
    for j in range(1,i+1):
        print(chr(b),end="")
        b=b+1
    print("\n")
