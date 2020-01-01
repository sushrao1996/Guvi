n1=int(input("Enter interval1 : "))
n2=int(input("Enter interval2 : "))
def strong_func(n1,n2):
    l1=[]
    for i in range(n1,n2+1):
        l=[]
        for j in str(i):
            l.append(j)
        sum=0
        for k in l:
            b=1
            for m in range(int(k),0,-1):
                b=b*m
            sum+=b
        if sum==i:
            l1.append(i)
    print(l1)
strong_func(n1,n2)
            
            
