a=input("Enter a number : ")
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(int(a[i]))
for i in b:
    print(i,end="")
    
