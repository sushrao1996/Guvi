def prime_func(interval1,interval2):
    l1=[]
    for i in range(interval1,interval2+1):
        l=[]
        for j in range(1,i+1):
            if i%j==0:
                l.append(j)
        if len(l)==2:
            l1.append(i)
    print("Prime Numbers are : ",l1)
    
n1=int(input("Enter interval1 : "))
n2=int(input("Enter interval2 : "))
prime_func(n1,n2)
