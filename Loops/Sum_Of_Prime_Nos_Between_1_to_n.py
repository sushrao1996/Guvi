a=input("Enter a number : ")
c=[]
if (int(a)==1):
    print("No prime numbers between 1 and " + str(a))
else:
    for i in range(1,int(a)+1):
        b=[]
        for j in range(1,int(a)+1):
            if (i%j==0):
                b.append(j)
        if (len(b)==2):
            c.append(str(i))
    b=0
    for j in c:
        b+=int(j)
    print(b)
        
    
