a=input("Enter a Number : ")
b=[]
#finding factors of the given number
for i in range(0,int(a)+1):
    for j in range(1,int(a)+1):
        if i*j==int(a):
            b.append(i)
#finding prime numbers upto the given number
c=[]
if (int(a)==1) or (int(a)==0):
    print("It has no prime factors")
else:
    for i in range(2,int(a)+1):
        d=[]
        for j in range(1,int(a)+1):
            if (i%j==0):
                d.append(j)
        if (len(d)==2):
            c.append(i)
#if factors are present in the prime number list then they are prime factors
    e=[]
    for i in b:
        if i in c:
            e.append(i)
    print(e)

