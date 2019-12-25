a=input("Enter number of rows : ")
for i in range(1,int(a)+1):
    for j in range(1,i+1):
            print('*',end="")
    print("\n")
for i in range(int(a)-1,0,-1):
    for j in range(i,0,-1):
            print('*',end="")
    print("\n")
