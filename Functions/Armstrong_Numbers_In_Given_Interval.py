def armstrong_func(interval1,interval2):
    l1=[]
    for i in range(interval1,interval2+1):
        l=[]
        for j in str(i):
            j=int(j)
            l.append(j)
        print(l)
        b=0
        for k in l:
            b += k*k*k
        print(i)
        print(b)
        if i==b:
            l1.append(i)
    print("Armstrong Numbers in the range are : ",l1)

n1=int(input("Enter interval1: "))
n2=int(input("Enter interval2: "))
armstrong_func(n1,n2)
