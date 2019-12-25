a=int(input("Enter number of terms : "))
c=[0,1]
for i in range(2,a+1):
    c.append(c[i-1]+c[i-2])
print(c)
