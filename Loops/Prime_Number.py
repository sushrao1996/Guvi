a=input("Enter a number : ")
b=[]
for i in range(1,int(a)+1):
    if (int(a)%i==0):
        b.append(i)
if len(b)==2:
    print(a + " is a prime number")
else:
    print(a + " is not a prime number")
        
