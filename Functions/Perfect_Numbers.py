def perfect_func(num1,num2):
    l1=[]
    for i in range(num1,num2+1):
        l=[]
        for j in range(1,i):
            if i%j==0:
                l.append(j)
        sum=0
        for k in l:
            sum+=k
        if sum==i:
            l1.append(i)
    print(l1)    
n1=int(input("Enter interval1 : "))
n2=int(input("Enter interval2 : "))
perfect_func(n1,n2)

