a=input("Enter the number of rows: ")
b=64
for i in range(1,int(a)+1):
    b=b+1
    for j in range(1,i+1):
        print(chr(b),end="")
    print("\n")
