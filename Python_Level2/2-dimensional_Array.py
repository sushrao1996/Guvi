n=input("Enter 2 input : ")
l=n.split(",")
X=int(l[0])
Y=int(l[1])
l1=[]
for i in range(X):
    l=[]
    for j in range(Y):
        l.append(i*j)
    l1.append(l)
print(l1)
    
