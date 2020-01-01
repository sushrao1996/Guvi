def prime_func(num):
    l=[]
    for i in range(1,num+1):
        if num%i==0:
            l.append(i)
    if len(l)==2:
        print("The number is prime.")
    else:
        print("The Number is not prime.")
n=int(input("Enter a Number : "))
prime_func(n)
def armstrong_func(n):
    l=[]
    for i in str(n):
        i=int(i)
        l.append(i)
    b=0
    for i in l:
        b += i*i*i
    if n==b:
        print(str(n) + " is an Armstrong Number")
    else:
        print(str(n) + " is not an Armstrong Number")

armstrong_func(n)
def perfect_func(num):
    l=[]
    for i in range(1,num):
        if num%i==0:
            l.append(i)
    sum=0
    for i in l:
        sum+=i
    if sum==n:
        print("The given number is a Perfect Number.")
    else:
        print("The given number is not a perfect Number.")
perfect_func(n)
        
    
