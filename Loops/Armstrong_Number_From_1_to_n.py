a=input("Enter a number : ")
for i in range(1,int(a)+1):
    b=0
    for j in str(i):
        b+=int(j)*int(j)*int(j)
    if i==b:
        print(i)
