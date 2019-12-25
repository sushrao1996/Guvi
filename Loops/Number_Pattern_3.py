a=input("Enter number of rows : ")
for i in range(1,int(a)+1):
    for j in range(1,i+1):
            print(j,end="")
    print("\n")

for i in range(int(a)-1,-1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")
